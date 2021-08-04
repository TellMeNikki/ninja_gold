from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("ninjagold", views.ninjagold),
    path("goldengain/<place>", views.goldengain),
    path("reset", views.reset),
]
