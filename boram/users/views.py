from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from accounts.models import User
from articles.models import Article


def users(request):
    users = User.objects.all().order_by("id")
    # for user in users:
    #     print(user.username)
    context = {"users":users}
    return render(request, "users/users.html", context)


# def profile(request, username):
#     context = {"username": username, }
#     return render(request, "users/profile.html", context)

def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    articles = Article.objects.filter(author = member.pk)
    for article in articles:
        print(article.title)
    context = {"member": member, "articles":articles}
    return render(request, "users/profile.html", context)


@require_POST
def follow(request, user_id):
    print(user_id)
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if request.user != member:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", member.username)
    return redirect("accounts:login")
