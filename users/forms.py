from django import forms
from . import models


class LoginForm(forms.Form):
    ID = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        id = self.cleaned_data.get("ID")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=id)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("비밀번호가 틀렸습니다."))
        except models.User.DoesNotExist:
            self.add_error("ID", forms.ValidationError("ID를 찾을 수 없습니다."))
