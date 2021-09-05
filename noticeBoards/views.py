from noticeBoards.models import notice
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from . import models
import math


@login_required(login_url="/login/")
def home(request):
    template_name = "noticeBoards/notice.html"
    page = request.GET.get("page")
    datas = notice.objects.all()
    paginator = Paginator(datas, 3)
    notice_page = paginator.get_page(page)
    if request.method == "POST":
        notice.objects.create(
            title=request.POST["title"],
            type=request.POST["type"],
            content=request.POST["content"],
            department=request.POST["department"],
            writer=request.POST["writer"],
        )

    return render(
        request,
        template_name,
        {
            "notices": notice_page,
        },
    )


def notice_detail(request):
    return render(request, "noticeBoards/noticeDetail.html")
