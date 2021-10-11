import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import JsonResponse
from django.shortcuts import render
from . import models
from classs import models as class_model
from registrations import models as regist_model
from classs import views as class_view


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
    else:
        return render(request, template_name)


def send_to_regi(request):
    jsonObject = json.loads(request.body)
    target_pk = jsonObject.get("id")
    target = class_model.Class.objects.get(pk=target_pk)
    target_time = target.time.replace(" ", "")
    user_data = models.List.objects.get(user=request.user)
    user_list = models.List.objects.get(user=request.user).subjects
    user_time_table = models.List.objects.get(user=request.user).time_table
    split_subject_time = []
    if "/" in target_time:
        split_subject_time = target_time.split("/")
    if len(split_subject_time) == 0:
        if target_time[1] == "(":
            new_data = class_view.change_time_data(target_time[2:])
            user_data.time_table[target_time[0]].remove(new_data)
            user_data.save()
        else:
            for i in target_time:
                if i.isdigit():
                    user_data.time_table[target_time[0]].remove(i)
                    user_data.save()
    else:
        for split_data in split_subject_time:
            if split_data[1] == "(":
                new_data = class_view.change_time_data(split_data[2:])
                user_data.time_table[split_data[0]].remove(new_data)
                user_data.save()
            else:
                for i in split_data:
                    if i.isdigit():
                        user_data.time_table[split_data[0]].remove(i)
                        user_data.save()
    user_list.remove(target)

    regi_list = regist_model.registration.objects.get_or_none(user=request.user)
    if regi_list is None:
        new_list = regist_model.registration.objects.create(user=request.user)
        new_list.subjects.add(target)
    else:
        regi_list.subjects.add(target)
    non_data = {}
    return JsonResponse(non_data)