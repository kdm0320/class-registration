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


class SignupForm(forms.Form):
    GRADE_FIRST = "1"
    GRADE_SECOND = "2"
    GRADE_THIRD = "3"
    GRADE_FOURTH = "4"

    GRADE_CHOICES = (
        (GRADE_FIRST, "1"),
        (GRADE_SECOND, "2"),
        (GRADE_THIRD, "3"),
        (GRADE_FOURTH, "4"),
    )
    ID = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
    password1 = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")
    last_name = forms.CharField(max_length=20, label="성")
    first_name = forms.CharField(max_length=20, label="이름")
    number = forms.IntegerField(label="학번")
    major = forms.CharField(max_length=30, label="전공")
    grade = forms.ChoiceField(choices=GRADE_CHOICES, label="학년")

    def clean_id(self):
        id = self.cleaned_data.get("username")
        try:
            models.User.objects.get(username=id)
            raise forms.ValidationError("이미 존재하는 ID 입니다.")
        except models.User.DoesNotExist:
            return id

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("이미 존재하는 Email 입니다.")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        else:
            return password

    def save(self):
        last_name = self.cleaned_data.get("last_name")
        first_name = self.cleaned_data.get("first_name")
        number = self.cleaned_data.get("number")
        major = self.cleaned_data.get("major")
        grade = self.cleaned_data.get("grade")
        ID = self.cleaned_data.get("ID")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = models.User.objects.create_user(ID, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.number = number
        user.major = major
        user.grade = grade
        user.save()
