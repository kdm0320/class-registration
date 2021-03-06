from django.urls import path
from . import views

app_name = "baskets"

urlpatterns = [
    path("schedule", views.basket, name="basket"),
    path("registration", views.send_to_regi, name="regi"),
    path("delete", views.delete, name="delete"),
]
