from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):
	return render(request, "articles/index.html")

def articles(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {
        "articles": articles,
    }
    return render(request, "articles/articles.html", context)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article,}
    return render(request, "articles/article_detail.html", context)

def new(request):
    return render(request, "articles/new.html")

def delete(request, pk):
    # 글 삭제
    article = Article.objects.get(pk=pk)
    article.delete()
    # 글 삭제하면 목록으로 돌아감
    return redirect("articles:articles")

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    article = Article.objects.create(title=title, content=content)
    return redirect("articles:article_detail", article.pk)