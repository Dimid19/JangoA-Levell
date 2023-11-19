from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main(request):
    return HttpResponse("Hey! It's your main page site!!")


def about(request):
    return HttpResponse("This page about your site !!")


def article_page(request):
    return HttpResponse("Hey! It's your details article page !!")


def article_comment(request, article_id):
    return HttpResponse(f"Hey! It's your  for {article_id} comments!!")


def article_create(request):
    return HttpResponse("Hey! It's your article_create page!!")


def article_update(request, article_id):
    return HttpResponse(f"Hey! It's your article {article_id} update page!!")


def article_delete(request, article_id):
    return HttpResponse(f"Hey! It's your article {article_id} delete page!!")
