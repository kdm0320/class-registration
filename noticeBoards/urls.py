from django.urls import path
from . import views as board_views

app_name = "notices"

urlpatterns = [
    path("", board_views.home, name="board"),
]
