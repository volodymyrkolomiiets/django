from django.urls import path
from . import views


app_name = "newapp"

urlpatterns = [
    path("home1/", views.home1, name='home1'),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login")
    
]