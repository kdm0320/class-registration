from django.urls import path
from . import views as board_views

app_name = "notices"

urlpatterns = [
    path("", board_views.NoticeView.as_view(), name="board"),
    path("myboard/", board_views.MyNoticeView.as_view(), name="find"),
    path("notce/<int:pk>/", board_views.NoticeDetail.as_view(), name="detail"),
]
