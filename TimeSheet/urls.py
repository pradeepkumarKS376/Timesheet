from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="Login"),
    path("inserttimesheet", views.inserttimesheet_view, name="inserttimesheet"),
    path("logouts", views.logout_view, name="logouts"),
]
