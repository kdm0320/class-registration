import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from . import models


def class_to_dictionary(data):
    output = {}
    output["pk"] = data.pk
    output["universe"] = data.universe
    output["check_major"] = data.check_major
    output["subject_number"] = data.subject_number
    output["subject_name"] = data.subject_name
    output["credit"] = data.credit
    output["professor"] = data.professor
    output["time"] = data.time
    output["department"] = data.department

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
