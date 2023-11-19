from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.


def main(request: HttpRequest):
    return HttpResponse("Hey! It's your main view!!")


def page_view(request: HttpRequest):
    return HttpResponse("Hey! It's your base page view!!")


def page_info_view(request: HttpRequest, page_id, name=""):
    return HttpResponse(f"Hey! It's your {page_id} page view with name {name}!!")


def page_uniq_view(request: HttpRequest):
    return HttpResponse(f"Hey! It's your unique 22 page view!!")