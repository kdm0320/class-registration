from noticeBoards.models import notice
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def home(request):
    template_name = "noticeBoards/notice.html"
    notices = serializers.serialize(
        "json",
        notice.objects.all(),
        fields=(
            "title",
            "type",
            "content",
            "department",
            "writer",
            "created",
            "post_hit",
        ),
    )
    return render(request, template_name, {"notices": notices})
