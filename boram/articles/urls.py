from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "articles"
urlpatterns = [
    path("index/", views.index, name="index"),
    # 글 목록 페이지
    path("", views.articles, name="articles"),
    # 상세 페이지
    path("<int:pk>/", views.article_detail, name="article_detail"),
    # 글 작성 페이지
    path("create/", views.create, name="create"),
    # 글 삭제
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/like/", views.like, name="like"),
    path(
        "<int:pk>/comments/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    # 글 검색
    path("search/", views.search, name="search"),
]
