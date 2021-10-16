import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import JsonResponse
from django.shortcuts import render
from . import models
from basketLists import models as basket_model


def class_to_dictionary(data):
    output = {}
    output["pk"] = data.pk
    output["universe"] = data.universe
    output["department"] = data.department
    output["grade"] = data.grade
    output["check_major"] = data.check_major
    output["subject_number"] = data.subject_number
    output["subject_name"] = data.subject_name
    output["credit"] = data.credit
    output["professor"] = data.professor
    output["time"] = data.time
    output["people"] = data.people
    return output


def change_time_data(time_data):

    if time_data[2:4] == "09":
        new_data = "A"
        return new_data
    elif time_data[2:4] == "10":
        new_data = "B"
        return new_data
    elif time_data[2:4] == "12":
        new_data = "C"
        return new_data
    elif time_data[2:4] == "13":
        new_data = "D"
        return new_data
    elif time_data[2:4] == "15":
        new_data = "E"
        return new_data
    elif time_data[2:4] == "16":
        new_data = "F"
        return new_data
    elif time_data[2:4] == "18":
        new_data = "G"
        return new_data
    elif time_data[2:4] == "19":
        new_data = "H"
        return new_data
    elif time_data[2:4] == "21":
        new_data = "ND"
        return new_data
    elif time_data[2:4] == "22":
        new_data = "SC"
        return new_data


def home(request):
    template_name = "class/viewSchedule.html"

    return render(
        request,
        template_name,
    )


def change_name(college):
    colleage = ""
    if college == "economics":
        colleage = "경제학부(서울)"
    elif college == "electronic":
        colleage = "전자전기공학부"
    elif college == "software":
        colleage = "소프트웨어학부"
    return colleage


def get_data(request):
    template_name = "class/viewSchedule.html"
    colleage = request.GET.get("college")
    depart = change_name(colleage)
    data = models.Class.objects.filter(department=depart).order_by("grade")
    temp_data = {}
    for i in range(len(data)):
        temp_data[f"class{i}"] = class_to_dictionary(data[i])

    datas = json.dumps(temp_data, ensure_ascii=False, cls=DjangoJSONEncoder)
    return render(request, template_name, {"class_data": datas})


def check_data(time_data, basket_list, numbers_to_alpha, check_schedule):
    for time in time_data[1:]:
        if (
            time.isdigit()
            and (numbers_to_alpha[time] in basket_list.time_table[time_data[0]])
            or (time in basket_list.time_table[time_data[0]])
        ):
            check_schedule.append(True)
            break


def regi_data(time_data, subject, basket_list):
    basket_list.subjects.add(subject)
    for time in time_data[1:]:
        if time.isdigit():
            basket_list.time_table[time_data[0]].append(time)


def create_data(time_data, new_basket):
    if time_data[1] == "(":
        new_data = change_time_data(time_data[2:])
        new_basket.time_table = new_basket.time_table[time_data[0]].append(new_data)
    else:
        for i in time_data:
            if i.isdigit():
                new_basket.time_table[time_data[0]].append(i)


def regi_basket(request):
    jsonObject = json.loads(request.body)
    target_pk = jsonObject.get("pk")
    basket_list = basket_model.List.objects.get_or_none(user=request.user)
    subject = models.Class.objects.get(pk=target_pk)
    subject_time = subject.time.replace(" ", "")
    split_subject_time = []
    if "/" in subject_time:
        split_subject_time = subject_time.split("/")

    alpha_to_numbers = {
        "A": ["1", "2"],
        "B": ["3"],
        "C": ["4", "5"],
        "D": ["6"],
        "E": ["7", "8"],
        "F": ["9"],
        "G": ["10", "11"],
        "H": ["12"],
        "ND": ["13", "14"],
        "SC": ["15"],
    }
    numbers_to_alpha = {
        "1": "A",
        "2": "A",
        "3": "B",
        "4": "C",
        "5": "C",
        "6": "D",
        "7": "E",
        "8": "E",
        "9": "F",
        "10": "G",
        "11": "G",
        "12": "H",
        "13": "ND",
        "14": "ND",
        "15": "SC",
    }
    if basket_list is None:
        new_basket, created = basket_model.List.objects.get_or_create(user=request.user)
        new_basket.subjects.add(subject)
        if len(split_subject_time) == 0:
            create_data(subject_time, new_basket)
        else:
            for split_data in split_subject_time:
                create_data(split_data, new_basket)
        new_basket.save()
    else:
        if len(split_subject_time) == 0:
            check_schedule = []
            check_data(subject_time, basket_list, numbers_to_alpha, check_schedule)
            if True not in check_schedule:
                regi_data(subject_time, subject, basket_list)
        else:
            check_schedule = []
            if split_subject_time[0][1] == "(":
                for split_data in split_subject_time:
                    new_data = change_time_data(split_data)
                    for number in alpha_to_numbers[new_data]:
                        if (number in basket_list.time_table[split_data[0]]) or (
                            new_data in basket_list.time_table[split_data[0]]
                        ):
                            check_schedule.append(True)
                if True not in check_schedule:
                    basket_list.subjects.add(subject)
                    for split_data in split_subject_time:
                        new_data = change_time_data(split_data)
                        basket_list.time_table[split_data[0]].append(new_data)
            else:
                for split_data in split_subject_time:
                    check_data(
                        split_data, basket_list, numbers_to_alpha, check_schedule
                    )

                    if True not in check_schedule:
                        regi_data(split_data, subject, basket_list)
            check_schedule = []
        basket_list.save()
    return JsonResponse(jsonObject)
