from django.urls import path
from .views import main, page_view, page_info_view, page_uniq_view

urlpatterns = [
    path("", main),
    path("page/", page_view, name="page"),
    path('page/22/', page_uniq_view, name='page_unique'),
    path('page/<int:page_id>/<str:name>', page_info_view, name='page_info_with_name'),
    path('page/<int:page_id>/', page_info_view, name='page_info'),
]