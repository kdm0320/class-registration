import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import JsonResponse
from django.shortcuts import render
from . import models
from basketLists import models as basket_model
from django.contrib import messages


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


def regi_basket(request):
    jsonObject = json.loads(request.body)
    target_sub_num = jsonObject.get("subject_number")
    basket_list = basket_model.List.objects.get_or_none(user=request.user)
    subject = models.Class.objects.get(subject_number=target_sub_num)
    if basket_list is None:
        new_basket, created = basket_model.List.objects.get_or_create(user=request.user)
        new_basket.subjects.add(subject)
    else:
        time_data_list = []
        time_datas = basket_list.subjects.values("time")
        for data in time_datas:
            time_data_list.append(list(data.values()))
        for data in time_data_list:
            if subject.time in data:
                messages.error(request, "같은 시간의 과목이 이미 장바구니에 존재합니다")
                break
            else:
                basket_list.subjects.add(subject)
                break

    return JsonResponse(jsonObject)
