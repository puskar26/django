from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.firstapp_home, name = 'app_home' ),
    path("login/", views.login, name = 'login' ),
]