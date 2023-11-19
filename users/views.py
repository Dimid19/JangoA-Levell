from django.shortcuts import render
from django.http import HttpResponse


def users_page(requests, username):
    return HttpResponse(f"Hey! This Personal page of the site {username}.")


def set_password(request):
    return HttpResponse("Hey! This route will use for change users credentials")


def set_userdata(requests):
    return HttpResponse("Hey! This route will be used to modify user data.")


def deactivate(requests):
    return HttpResponse("Hey! This page deactivate users(delete)!!")


def register(requests):
    return HttpResponse("Hey! This page register users!!")


def login(requests):
    return HttpResponse("Hey! This page login users!!")


def logout(requests):
    return HttpResponse("Hey! This page logout users!!")

