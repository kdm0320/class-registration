import json
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import JsonResponse
from django.shortcuts import render
from . import models
from classs import models as class_model


@login_required(login_url="users/login/")
def enrollment(request):
    template_name = "enrolment.html"

    lists = models.registration.objects.get_or_none(user=request.user)
    if lists:
        data = lists.subjects.values()
        temp_data = {}
        for i in range(len(data)):
            temp_data[f"class{i}"] = data[i]
        datas = json.dumps(temp_data, ensure_ascii=False, cls=DjangoJSONEncoder)

        return render(request, template_name, {"regi_datas": datas})
    else:
        return render(request, template_name)


def delete(request):
    jsonObject = json.loads(request.body)
    target_list = models.registration.objects.get(user=request.user).subjects
    target_pk = jsonObject.get("id")
    target_name = class_model.Class.objects.get(id=target_pk)
    target_list.remove(target_name)
    non_data = {}
    return JsonResponse(non_data)
