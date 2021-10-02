from django.urls import path
from . import views

app_name = "baskets"

urlpatterns = [
    path("schedule", views.basket, name="basket"),
    path("registaration", views.send_to_regi, name="regi"),
]