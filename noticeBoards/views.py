from noticeBoards.models import notice
from django.shortcuts import redirect, render
from django.views.generic import ListView

# from django.contrib.auth.decorators import login_required


class noticeView(ListView):
    """noticeView Definition"""

    model = notice
    paginate_by = 3
    ordering = "created"
    context_object_name = "notices"

    def post(self, request):
        notice.objects.create(
            title=request.POST["title"],
            type=request.POST["type"],
            content=request.POST["content"],
            department=request.POST["department"],
            writer=request.POST["writer"],
        )

        return redirect("notices:board")


# @login_required(login_url="/login/")
# def home(request):
#     template_name = "noticeBoards/notice_list.html"
#     page = request.GET.get("page", 1)
#     datas = notice.objects.all()
#     paginator = Paginator(datas, 3, orphans=1)

#     notice_page = paginator.get_page(page)
#     if request.method == "POST":
#         notice.objects.create(
#             title=request.POST["title"],
#             type=request.POST["type"],
#             content=request.POST["content"],
#             department=request.POST["department"],
#             writer=request.POST["writer"],
#         )
#     return render(
#         request,
#         template_name,
#         {
#             "notices": notice_page,
#         },
#     )


def notice_detail(request, pk):
    return render(request, "noticeBoards/noticeDetail.html")
