import json
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import JsonResponse
from django.shortcuts import render
from . import models
from classs import models as class_model
from basketLists import views as basket_view


@login_required
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


@login_required
def delete(request):
    jsonObject = json.loads(request.body)
    user_list = models.registration.objects.get(user=request.user)
    target_pk = jsonObject.get("id")
    target = class_model.Class.objects.get(id=target_pk)
    target_time = target.time.replace(" ", "")
    split_subject_time = []
    if "/" in target_time:
        split_subject_time = target_time.split("/")

    delete_time = basket_view.HandleRegiTimeData()

    if len(split_subject_time) == 0:
        user_list.subjects.remove(target)
        delete_time.remove_data(target_time, user_list)
        user_list.credits -= float(target.credit)
    else:
        for split_data in split_subject_time:
            delete_time.remove_data(split_data, user_list)
        user_list.subjects.remove(target)
        user_list.credits -= float(target.credit)

    user_list.save()
    credit_data = {"credit": f"{user_list.credits}"}

    return JsonResponse(credit_data)