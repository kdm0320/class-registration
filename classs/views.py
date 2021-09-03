from django.shortcuts import render
from . import models
from django.core import serializers


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
    datas = serializers.serialize(
        "json",
        data,
        fields=(
            "grade",
            "check_major",
            "subject_number",
            "subject_name",
            "credit",
            "professor",
            "time",
            "universe",
            "department",
        ),
    )
    return render(request, template_name, {"class_data": datas})