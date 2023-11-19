from django.urls import path
from .views import topics_page, topics_subscribe, topics_unsubscribe

urlpatterns = [
    path("", topics_page),
    path("<int:topics_id>/topics_subscribe/", topics_subscribe),
    path("<int:topics_id>/topics_unsubscribe/", topics_unsubscribe),
]