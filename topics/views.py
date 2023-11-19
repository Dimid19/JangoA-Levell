from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def topics_page(request):
    return HttpResponse("Hey! It's your topics themes site")


def topics_subscribe(request, topics_id):
    return HttpResponse(f"Hey! It's your view to subscribe {topics_id} to a topic")


def topics_unsubscribe(request, topic_id):
    return HttpResponse(f"Hey! It's your  view to unsubscribe {topic_id} to a topic.")