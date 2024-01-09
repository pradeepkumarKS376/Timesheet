from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="Login"),
    path("inserttimesheet", views.inserttimesheet_view, name="inserttimesheet"),
    path("logouts", views.logout_view, name="logouts"),
    path("delete/<id>", views.del_view),
    path("update/<id>", views.edit_view,name ="updates"),
    path("Adminref", views.AdminRef_view, name="Adminref"),
]
