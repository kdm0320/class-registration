from django.urls import path
from . import views as board_views

app_name = "notices"

urlpatterns = [
    path("", board_views.NoticeView.as_view(), name="board"),
    path("myboard/", board_views.MyNoticeView.as_view(), name="find"),
    path("notice/<int:pk>/", board_views.notice_detail, name="detail"),
    path("search/", board_views.SeachView.as_view(), name="search"),
    path("delete/<int:pk>/", board_views.delete, name="delete"),
    path("save/<int:pk>/", board_views.save, name="save"),
]
