from django.urls import path
from . import views as board_views

app_name = "notices"

urlpatterns = [
    path("", board_views.noticeView.as_view(), name="board"),
    path("", board_views.notice_detail, name="detail"),
]
