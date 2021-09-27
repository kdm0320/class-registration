from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("enrollment", views.enrollment, name="enrollment"),
    path("logout", views.log_out, name="logout"),
    path("schedule", views.user_schedule, name="schedule"),
]