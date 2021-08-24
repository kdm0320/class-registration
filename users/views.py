from django.http import response
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views import View
from django.views.generic import FormView

from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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
                return redirect("users:enrollment")

        return render(request, "index.html", {"form": form})


# def index(request):
#     if request.COOKIES.get("username") is not None:
#         response = render(request, "index.html")
#         response.delete_cookie("username")
#         response.delete_cookie("password")
#         logout(request)
#         return response


# def log_in(request):
#     if request.user.is_authenticated:
#         return redirect("users:enrollment")

#     if request.method == "POST":
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect("core:index")
#     else:
#         form = AuthenticationForm()
#     return render(request, "index.html", {"form": form})


def log_out(request):

    logout(request)

    return redirect("core:index")


def enrollment(request):
    template_name = "users/enrolment.html"
    try:
        return render(
            request, template_name, {"is_login": request.session["_auth_user_id"]}
        )
    except KeyError:
        return redirect("core:error")


def basket(request):
    template_name = "users/basket.html"
    try:
        return render(
            request, template_name, {"is_login": request.session["_auth_user_id"]}
        )
    except KeyError:
        return redirect("core:error")


def user_schedule(request):
    template_name = "users/userSchedule.html"

    try:
        return render(
            request, template_name, {"is_login": request.session["_auth_user_id"]}
        )
    except KeyError:
        return redirect("core:error")
