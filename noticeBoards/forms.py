from django import forms
from django.forms.widgets import Textarea


class NoticForm(forms.Form):
    title = forms.CharField(label="제목", min_length=3, max_length=20)
    options = (("Notice", "공지"), ("Question", "문의"))
    type = forms.ChoiceField(label="종류", choices=options)
    content = forms.CharField(label="내용", widget=Textarea)
    department = forms.CharField(label="소속", max_length=10)
    writer = forms.CharField(label="작성자")
