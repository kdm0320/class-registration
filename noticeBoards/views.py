from noticeBoards.models import notice
from django.shortcuts import redirect, render
from django.urls.base import reverse
from .models import notice

ERROR_PAGE = "core:error"


def home(request):
    template_name = "noticeBoards/notice.html"
    try:

        return render(
            request, template_name, {"is_login": request.session["_auth_user_id"]}
        )
    except KeyError:
        return redirect(reverse(ERROR_PAGE))
