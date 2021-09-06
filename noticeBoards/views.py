#from noticeBoards.models import notice
#from django.shortcuts import redirect, render
#from django.urls.base import reverse
#from django.core import serializers
#from django.contrib.auth.decorators import login_required

#@login_required(login_url="/login/")
# def home(request):
#    template_name = "noticeBoards/notice.html"
#    notices = serializers.serialize(
#        "json",
#        notice.objects.all(),
#        fields=(
#            "title",
#            "type",
#            "content",
#            "department",
#            "writer",
#            "created",
#            "post_hit",
#        ),
#    )
#    return render(request, template_name, {"notices": notices})


from noticeBoards.models import notice
from django.shortcuts import redirect, render
from django.views.generic import ListView


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


def notice_detail(request, pk):
    return render(request, "noticeBoards/noticeDetail.html")