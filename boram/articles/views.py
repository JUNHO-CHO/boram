from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm



# Create your views here.


def index(request):
    return render(request, "articles/index.html")

# 글 목록 페이지


def articles(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {
        "articles": articles,
    }
    return render(request, "articles/articles.html", context)


# 글 상세페이지
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article, }
    return render(request, "articles/article_detail.html", context)

# 글 작성 페이지
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.Files)
        if form.is_valid():
            article = form.save(submit=False)
            article.author = request.user
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "articles/create.html", context)

# 글 수정페이지


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm(isinstance=article)

    context = {
        "form": form,
        "article": article,
    }
    return render(request, "articles/update.html", context)

# 글 삭제


def delete(request, pk):
    # 글 삭제
    article = Article.objects.get(pk=pk)
    article.delete()
    # 글 삭제하면 목록으로 돌아감
    return redirect("articles:articles")


def like(request, pk):
    return redirect("articles:articles")
