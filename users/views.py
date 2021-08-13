from django.shortcuts import render
from django.views import View
from . import forms
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
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
                return render(request, "regIndex.html")

        return render(request, "index.html", {"form": form})
