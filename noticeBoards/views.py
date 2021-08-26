from noticeBoards.models import notice
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.core import serializers

ERROR_PAGE = "core:error"


def home(request):
    template_name = "noticeBoards/notice.html"
    try:
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
        return render(
            request,
            template_name,
            {"is_login": request.session["_auth_user_id"], "notices": notices},
        )
    except KeyError:
        return redirect(reverse(ERROR_PAGE))
