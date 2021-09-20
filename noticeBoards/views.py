from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from noticeBoards.models import notice
from django.shortcuts import redirect, render
from django.views.generic import ListView, View


class NoticeView(ListView):
    """NoticeView Definition"""

    def get(self, request):
        template_name = "noticeBoards/notice_list.html"
        page = request.GET.get("page", 1)
        datas = notice.objects.all().order_by("created")
        paginator = Paginator(datas, 3, orphans=1)
        notice_page = paginator.get_page(page)
        self.request.session["current_url"] = request.get_full_path()

        return render(
            request,
            template_name,
            {
                "notices": notice_page,
            },
        )

    def post(self, request):
        notice_writer = request.user.last_name + request.user.first_name
        writer_deaprtment = request.user.major
        notice.objects.create(
            title=request.POST["title"],
            type=request.POST["type"],
            content=request.POST["content"],
            department=writer_deaprtment,
            writer=notice_writer,
        )

        return redirect("notices:board")


class MyNoticeView(ListView):
    """MyNoticeView Definition"""

    template_name = "noticeBoards/my_notice_list.html"
    model = notice
    paginate_by = 3
    ordering = "created"
    context_object_name = "notices"

    def get_queryset(self, **kwargs):
        user = f"{self.request.user.last_name}{self.request.user.first_name}"
        user_notice = notice.objects.filter(writer=user)
        return user_notice

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


# class NoticeDetail(DetailView):

#     """NoticeDetail Definition"""

#     model = notice
#     context_object_name = "notice"


def notice_detail(request, pk):
    template_name = "noticeBoards/notice_detail.html"
    try:
        target_notice = notice.objects.get(pk=pk)
        target_notice.post_hit += 1
        target_notice.save()
        return render(request, template_name, {"notice": target_notice})
    except notice.DoesNotExist:
        raise Http404()


class SeachView(ListView):
    template_name = "noticeBoards/notice_search.html"
    paginate_by = 3
    ordering = "created"
    context_object_name = "target"

    def get_queryset(self, **kwargs):
        title = self.request.GET.get("search")
        if title is not None:
            self.request.session["search_word"] = title
            filter_args = {"title__startswith": title}
            target_notices = notice.objects.filter(**filter_args)
            return target_notices
        else:
            filter_args = {"title__startswith": self.request.session["search_word"]}
            target_notices = notice.objects.filter(**filter_args)
            return target_notices


# def search(request):
#     template_name = "noticeBoards/notice_search.html"
#     title = request.GET.get("search")
#     page = request.GET.get("page", 1)
#     if title is not None:
#         global title_list
#         title_list = title
#         filter_args = {"title__startswith": title}
#         target_notices = notice.objects.filter(**filter_args)
#         paginator = Paginator(target_notices, 3)
#         notice_page = paginator.get_page(page)
#         return render(
#             request, template_name, {"target": notice_page, "search_title": title}
#         )
#     else:
#         filter_args = {"title__startswith": title_list}
#         target_notices = notice.objects.filter(**filter_args)
#         paginator = Paginator(target_notices, 3)
#         notice_page = paginator.get_page(page)
#         return render(
#             request, template_name, {"target": notice_page, "search_title": title}
#         )


def save(request, pk):
    target = notice.objects.get(pk=pk)
    target.title = request.POST.get("detail_title_data")
    target.content = request.POST.get("detail_area_data")
    target.save()

    current_url = request.GET.get("next")
    print(current_url)
    return redirect(current_url)


def delete(request, pk):
    target = notice.objects.get(pk=pk)
    target.delete()
    return redirect(request.session["current_url"])
