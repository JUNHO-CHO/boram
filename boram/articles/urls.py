from django.contrib import admin
from django.urls import path, include
from . import views

app_name="articles"
urlpatterns = [
    path("index/", views.index, name = "index"),
    path("",views.articles, name="articles"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("new/",views.new, name="new"),
    path("create/",views.create, name="create"),
    path("<int:pk>/delete/", views.delete, name="delete"),
]
