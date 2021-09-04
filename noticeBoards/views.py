from django.core.serializers.json import DjangoJSONEncoder
from noticeBoards.models import notice
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.contrib.auth.decorators import login_required
from . import forms
import json


def blogToDictionary(blog):
    """
    A utility function to convert object of type Blog to a Python Dictionary
    """
    output = {}
    output["pk"] = blog.pk
    output["title"] = blog.title
    output["type"] = blog.type
    output["content"] = blog.content
    output["department"] = blog.department
    output["writer"] = blog.writer
    output["created"] = blog.created
    output["post_hit"] = blog.post_hit

    return output


@login_required(login_url="/login/")
def home(request):
    template_name = "noticeBoards/notice.html"
    notice_form = forms.NoticForm()
    datas = notice.objects.all()
    tempBlogs = {}
    for i in range(len(datas)):
        tempBlogs[f"data{i}"] = blogToDictionary(datas[i])
    notices = json.dumps(tempBlogs, ensure_ascii=False, cls=DjangoJSONEncoder)
    if request.method == "POST":
        print(request.POST)

    return render(request, template_name, {"notices": notices, "form": notice_form})


def notice_detail(request):
    return render(request, "noticeBoards/noticeDetail.html")
