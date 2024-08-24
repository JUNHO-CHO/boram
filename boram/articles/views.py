from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, "articles/index.html")


def articles(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {
        "articles": articles,
    }
    return render(request, "articles/articles.html", context)


@login_required
def new(request):
    if request.user:
        return render(request, "articles/new.html")
    return redirect("accounts:")


def create(request):
    article = Article()
    article.title = request.POST.get("title")
    article.content = request.POST.get("content")
    article.author = request.user
    article.save()
    return redirect("articles:article_detail", article.pk)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article, }
    return render(request, "articles/article_detail.html", context)


def update(request, pk):
    return redirect("articlles:articles")


def delete(request, pk):
    # 글 삭제
    article = Article.objects.get(pk=pk)
    article.delete()
    # 글 삭제하면 목록으로 돌아감
    return redirect("articles:articles")


def like(request, pk):
    return redirect("articles:articles")
