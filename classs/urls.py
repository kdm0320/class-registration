from django.urls import path
from . import views as class_views

app_name = "classes"

urlpatterns = [
    path("schdules/", class_views.home, name="class"),
    path("data/", class_views.get_data, name="lookup"),
]
