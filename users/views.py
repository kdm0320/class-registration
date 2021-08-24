from django.http import response
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views import View
from django.views.generic import FormView
from . import forms
from . import models
from django.contrib.auth import authenticate, login, logout


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
                return redirect(reverse("users:enrollment"))

        return render(request, "index.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("core:index"))


ERROR_PAGE = "core:error"


def enrollment(request):
    template_name = "users/enrolment.html"
    try:
        return render(
            request, template_name, {"is_login": request.session["_auth_user_id"]}
        )
    except KeyError:
        return redirect(reverse(ERROR_PAGE))


def basket(request):
    template_name = "users/basket.html"
    try:
        return render(
            request, template_name, {"is_login": request.session["_auth_user_id"]}
        )
    except KeyError:
        return redirect(reverse(ERROR_PAGE))


def user_schedule(request):
    template_name = "users/userSchedule.html"
    try:
        return render(
            request, template_name, {"is_login": request.session["_auth_user_id"]}
        )
    except KeyError:
        return redirect(reverse(ERROR_PAGE))
