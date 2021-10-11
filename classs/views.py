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

    if time_data[:2] == "09":
        new_data = "A"
        return new_data
    elif time_data[:2] == "10":
        new_data = "B"
        return new_data
    elif time_data[:2] == "12":
        new_data = "C"
        return new_data
    elif time_data[:2] == "13":
        new_data = "D"
        return new_data
    elif time_data[:2] == "15":
        new_data = "E"
        return new_data
    elif time_data[:2] == "16":
        new_data = "F"
        return new_data
    elif time_data[:2] == "18":
        new_data = "G"
        return new_data
    elif time_data[:2] == "19":
        new_data = "H"
        return new_data
    elif time_data[:2] == "21":
        new_data = "I"
        return new_data
    elif time_data[:2] == "22":
        new_data = "J"
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


def divded_data(new_data, user_data, subject_time, basket_list, subject):
    if new_data.isalpha() is False:
        try:
            if subject_time[1] == "1" or subject_time[1] == "2":
                if (
                    "A" in user_data.time_table[subject_time[0]]
                    or subject_time[1] in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    for i in subject_time:
                        if i.isdigit():
                            user_data.time_table[subject_time[0]].append(i)
                    user_data.save()
            elif subject_time[1] == "3":
                if (
                    "B" in user_data.time_table[subject_time[0]]
                    or subject_time[1] in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    for i in subject_time:
                        if i.isdigit():
                            user_data.time_table[subject_time[0]].append(i)
                    user_data.save()
            elif subject_time[1] == "4" or subject_time[1] == "5":
                if (
                    "C" in user_data.time_table[subject_time[0]]
                    or subject_time[1] in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    for i in subject_time:
                        if i.isdigit():
                            user_data.time_table[subject_time[0]].append(i)
                    user_data.save()
            elif subject_time[1] == "6":
                if (
                    "D" in user_data.time_table[subject_time[0]]
                    or subject_time[1] in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    for i in subject_time:
                        if i.isdigit():
                            user_data.time_table[subject_time[0]].append(i)
                    user_data.save()
            elif subject_time[1] == "7" or subject_time[1] == "8":
                if (
                    "E" in user_data.time_table[subject_time[0]]
                    or subject_time[1] in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    for i in subject_time:
                        if i.isdigit():
                            user_data.time_table[subject_time[0]].append(i)
                    user_data.save()
            elif subject_time[1] == "9":
                if (
                    "F" in user_data.time_table[subject_time[0]]
                    or subject_time[1] in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    for i in subject_time:
                        if i.isdigit():
                            user_data.time_table[subject_time[0]].append(i)
                    user_data.save()
            elif subject_time[1] == "10" or subject_time[1] == "11":
                if (
                    "G" in user_data.time_table[subject_time[0]]
                    or subject_time[1] in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    for i in subject_time:
                        if i.isdigit():
                            user_data.time_table[subject_time[0]].append(i)
                    user_data.save()
            elif subject_time[1] == "12":
                if (
                    "H" in user_data.time_table[subject_time[0]]
                    or subject_time[1] in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    for i in subject_time:
                        if i.isdigit():
                            user_data.time_table[subject_time[0]].append(i)
                    user_data.save()
            elif subject_time[1] == "13" or subject_time[1] == "14":
                if (
                    "I" in user_data.time_table[subject_time[0]]
                    or subject_time[1] in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    for i in subject_time:
                        if i.isdigit():
                            user_data.time_table[subject_time[0]].append(i)
                    user_data.save()
            elif subject_time[1] == "15":
                if (
                    "J" in user_data.time_table[subject_time[0]]
                    or subject_time[1] in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    for i in subject_time:
                        if i.isdigit():
                            user_data.time_table[subject_time[0]].append(i)
                    user_data.save()
        except KeyError:
            basket_list.subjects.add(subject)
            user_data.time_table[subject_time[0]] = []
            for i in subject_time:
                if i.isdigit():
                    user_data.time_table[subject_time[0]].append(i)
            user_data.save()
    else:
        try:
            if new_data == "A":
                if (
                    "1" in user_data.time_table[subject_time[0]]
                    or new_data in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    user_data.time_table[subject_time[0]].append(new_data)
                    user_data.save()
            elif new_data == "B":
                if (
                    "2" in user_data.time_table[subject_time[0]]
                    or new_data in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    user_data.time_table[subject_time[0]].append(new_data)
                    user_data.save()
            elif new_data == "C":
                if (
                    "4" in user_data.time_table[subject_time[0]]
                    or new_data in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    user_data.time_table[subject_time[0]].append(new_data)
                    user_data.save()
            elif new_data == "D":
                if (
                    "5" in user_data.time_table[subject_time[0]]
                    or new_data in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    user_data.time_table[subject_time[0]].append(new_data)
                    user_data.save()
            elif new_data == "E":
                if (
                    "7" in user_data.time_table[subject_time[0]]
                    or new_data in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    user_data.time_table[subject_time[0]].append(new_data)
                    user_data.save()
            elif new_data == "F":
                if (
                    "8" in user_data.time_table[subject_time[0]]
                    or new_data in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    user_data.time_table[subject_time[0]].append(new_data)
                    user_data.save()
            elif new_data == "G":
                if (
                    "10" in user_data.time_table[subject_time[0]]
                    or new_data in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    user_data.time_table[subject_time[0]].append(new_data)
                    user_data.save()
            elif new_data == "H":
                if (
                    "11" in user_data.time_table[subject_time[0]]
                    or new_data in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    user_data.time_table[subject_time[0]].append(new_data)
                    user_data.save()
            elif new_data == "I":
                if (
                    "13" in user_data.time_table[subject_time[0]]
                    or new_data in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    user_data.time_table[subject_time[0]].append(new_data)
                    user_data.save()
            elif new_data == "J":
                if (
                    "14" in user_data.time_table[subject_time[0]]
                    or new_data in user_data.time_table[subject_time[0]]
                ):
                    pass
                else:
                    basket_list.subjects.add(subject)
                    user_data.time_table[subject_time[0]].append(new_data)
                    user_data.save()
        except KeyError:
            basket_list.subjects.add(subject)
            user_data.time_table[subject_time[0]] = [new_data]
            user_data.save()


def regi_basket(request):
    jsonObject = json.loads(request.body)
    target_pk = jsonObject.get("pk")
    basket_list = basket_model.List.objects.get_or_none(user=request.user)
    subject = models.Class.objects.get(pk=target_pk)
    subject_time = subject.time.replace(" ", "")
    user_data = basket_model.List.objects.get(user=request.user)
    split_subject_time = []
    if "/" in subject_time:
        split_subject_time = subject_time.split("/")

    if basket_list is None:
        new_basket, created = basket_model.List.objects.get_or_create(user=request.user)
        new_basket.subjects.add(subject)
        if len(split_subject_time) == 0:
            if subject_time[1] == "(":
                new_data = change_time_data(subject_time[2:])
                user_data.time_table = {subject_time[0]: [new_data]}
                user_data.save()
            else:
                user_data.time_table = {subject_time[0]: []}
                user_data.save()
                for i in subject_time:
                    if i.isdigit():
                        user_data.time_table[subject_time[0]].append(i)
                        user_data.save()
        else:
            for split_data in split_subject_time:
                if split_data[1] == "(":
                    new_data = change_time_data(split_data[2:])
                    user_data.time_table = {split_data[0]: [new_data]}
                    user_data.save()
                else:
                    user_data.time_table = {split_data[0]: []}
                    user_data.save()
                    for i in subject_time:
                        if i.isdigit():
                            user_data.time_table[split_data[0]].append(i)
                            user_data.save()
    else:
        if len(split_subject_time) == 0:
            if subject_time[1] == "(":
                new_data = change_time_data(subject_time[2:])
                divded_data(new_data, user_data, subject_time, basket_list, subject)
            else:
                divded_data(subject_time, user_data, subject_time, basket_list, subject)
        else:
            for split_data in split_subject_time:
                if split_data[1] == "(":
                    new_data = change_time_data(split_data[2:])
                    divded_data(new_data, user_data, split_data, basket_list, subject)
                else:
                    divded_data(split_data, user_data, split_data, basket_list, subject)

    return JsonResponse(jsonObject)