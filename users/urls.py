from django.urls import path
from .views import users_page, set_password, set_userdata, deactivate, register, login, logout

urlpatterns = [
    path("profile/<str:username>/", users_page),
    path("set_password/", set_password),
    path("set_userdata/", set_userdata),
    path("deactivate/", deactivate),
    path("register/", register),
    path("login/", login),
    path("logout/", logout),
]

