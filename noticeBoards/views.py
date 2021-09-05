from noticeBoards.models import notice
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms, models
import math


@login_required(login_url="/login/")
def home(request):
    template_name = "noticeBoards/notice.html"
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 3
    limit = page_size * page
    offset = limit - page_size
    page_count = math.ceil(notice.objects.count() / page_size)
    datas = notice.objects.all()[offset:limit]
    if request.method == "POST":
        print(request.POST)

    return render(
        request,
        template_name,
        {
            "notices": datas,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
            "last_page": page_count,
        },
    )


def notice_detail(request):
    return render(request, "noticeBoards/noticeDetail.html")
