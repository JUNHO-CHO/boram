from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.db.models import Count


def index(request):
    return render(request, "articles/index.html")

# 글 목록 페이지
def articles(request):
    sort_by = request.GET.get('sort', 'latest')  # 기본값은 최신순

    if sort_by == 'oldest':
        articles = Article.objects.all().order_by("created_at")  # 오래된순
    elif sort_by == 'popular':
        articles = Article.objects.all().annotate(like_count=Count('likes')).order_by('-like_count', '-created_at')  # 인기도순
    else:
        articles = Article.objects.all().order_by("-created_at")  # 최신순

    context = {
        "articles": articles,
        "sort_by": sort_by,
    }
    return render(request, "articles/articles.html", context)


# 글 상세페이지
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article, }
    return render(request, "articles/article_detail.html", context)

@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article = form.save()
            return redirect("articles:article_detail", article.id)
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "articles/create.html", context)

# 글 수정페이지

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if article.author == request.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect("articles:article_detail", article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect("articles:articles")


    context = {
        "form": form,
        "article": article,
    }
    return render(request, "articles/update.html", context)

# 글 삭제

@require_POST
def delete(request, pk):
    # 글 삭제
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if article.author == request.user:
            article.delete()
    # 글 삭제하면 목록으로 돌아감
    return redirect("articles:articles")

@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user) # 좋아요 취소
        else:
            article.like_users.add(request.user) #좋아요
        return redirect("articles:articles") 
    return redirect("accounts:login") # 로그인 안했으면 로그인페이지로 돌아감

@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect("articles:article_detail", article.pk)


@require_POST
def comment_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
    return redirect("articles:article_detail", pk)