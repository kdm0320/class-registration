from django.urls import path
from . import views

app_name = "regist"

urlpatterns = [
    path("", views.enrollment, name="enrollment"),
    path("delete", views.delete, name="delete"),
]