from django.urls import path
from .views import main, about, article_page, article_comment, article_create, article_update, article_delete

urlpatterns = [
    path("", main),
    path("about/", about),
    path("article_page/", article_page),
    path("article_page/<int:article_id>/comment/", article_comment),
    path("create/", article_create),
    path("article_upd/<int:article_id>/update/", article_update),
    path("article_del/<int:article_id>/delete/", article_delete),
]