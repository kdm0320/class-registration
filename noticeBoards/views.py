from noticeBoards.models import notice
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


# @login_required(login_url="/login/")
class noticeView(ListView):
    """noticeView Definition"""

    model = notice
    paginate_by = 3
    ordering = "created"

    def post(self, request):
        notice.objects.create(
            title=request.POST["title"],
            type=request.POST["type"],
            content=request.POST["content"],
            department=request.POST["department"],
            writer=request.POST["writer"],
        )

        return redirect("notices:board")


# def home(request):
#     template_name = "noticeBoards/notice.html"
#     page = request.GET.get("page", 1)
#     datas = notice.objects.all()
#     paginator = Paginator(datas, 3, orphans=1)

#     if request.method == "POST":
#         notice.objects.create(
#             title=request.POST["title"],
#             type=request.POST["type"],
#             content=request.POST["content"],
#             department=request.POST["department"],
#             writer=request.POST["writer"],
#         )
#     try:
#         notice_page = paginator.page(int(page))
#         return render(
#             request,
#             template_name,
#             {
#                 "notices": notice_page,
#             },
#         )
#     except EmptyPage:
#         return redirect("notices:board")


def notice_detail(request):
    return render(request, "noticeBoards/noticeDetail.html")
