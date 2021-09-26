from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import FormView
from . import forms
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
                return redirect(reverse("users:enrollment"))
            return render(request, "index.html", {"form": form})


@login_required(login_url="/login/")
def log_out(request):
    logout(request)
    return redirect(reverse("core:index"))


@login_required(login_url="/login/")
def user_schedule(request):
    template_name = "users/userSchedule.html"
    return render(request, template_name)
