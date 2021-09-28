import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import JsonResponse
from django.shortcuts import render
from . import models
from classs import models as class_model
from registrations import models as regist_model


def class_to_dictionary(data):
    output = {}
    output["subject_number"] = data.subject_number
    output["subject_name"] = data.subject_name
    output["grade"] = data.grade
    output["check_major"] = data.check_major
    output["credit"] = data.credit
    output["professor"] = data.professor
    output["time"] = data.time
    output["people"] = data.people
    output["universe"] = data.universe
    output["department"] = data.department
    return output


def basket(request):
    template_name = "basket.html"
    lists = models.List.objects.get_or_none(user=request.user)
    if lists:
        data = lists.subjects.values()
        temp_data = {}
        for i in range(len(data)):
            temp_data[f"class{i}"] = data[i]
        datas = json.dumps(temp_data, ensure_ascii=False, cls=DjangoJSONEncoder)

        return render(request, template_name, {"basket_datas": datas})


def send_to_regi(request):
    jsonObject = json.loads(request.body)
    target_list = models.List.objects.get(user=request.user).subjects
    target_pk = jsonObject.get("id")
    target_name = class_model.Class.objects.get(pk=target_pk)
    target_list.remove(target_name)
    regi_list = regist_model.registration.objects.get_or_none(user=request.user)
    if regi_list is None:
        new_list = regist_model.registration.objects.create(user=request.user)
        new_list.subjects.add(target_name)
    else:
        regi_list.subjects.add(target_name)
    non_data = {}
    return JsonResponse(non_data)
