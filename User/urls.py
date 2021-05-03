from django.urls import path

from . import views

urlpatterns =[
    path("",views.index,name="index"),
    path("register",views.register,name="register"),
    path("login",views.view_login,name="login"),
    path("logout",views.view_logout,name="logout"),
    path("module",views.Choose_modl,name="module"),
]