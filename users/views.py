import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import FormView
from . import forms
from registrations import models as regist_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class LoginView(FormView):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "index.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("ID")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=id, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("regist:enrollment"))
            return render(request, "index.html", {"form": form})


@login_required
def log_out(request):
    logout(request)
    return redirect(reverse("core:index"))


@login_required
def user_schedule(request):
    template_name = "users/userSchedule.html"
    lists = regist_model.registration.objects.get(user=request.user)
    if lists:
        data = lists.subjects.values("subject_name", "time")
        temp_data = {}
        for i in range(len(data)):
            temp_data[f"class{i}"] = data[i]
        datas = json.dumps(temp_data, ensure_ascii=False, cls=DjangoJSONEncoder)

        return render(request, template_name, {"time_datas": datas})
    else:
        return render(request, template_name)