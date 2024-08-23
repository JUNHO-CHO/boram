from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.forms import ( 
    UserCreationForm,
    UserChangeForm,
)
from django.contrib.auth import update_session_auth_hash
from .forms import (
    CustomUserChangeForm,
    CustomUserCreationForm,
    PasswordConfirmationForm
)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            netx_url = request.GET.get("next") or "index"
            return redirect("articles:index")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("articles:index")


@require_http_methods(['GET','POST'])
def signup(request):
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form. is_valid():
            user=form.save()
            auth_login(request, user)
            return redirect("articles:index")
    else:
        form = CustomUserCreationForm()
    context = {"form":form}
    return render(request, "accounts/signup.html", context)


@require_POST
def delete(request):
    if request.method == "POST":
        form = PasswordConfirmationForm(request, data=request.POST)
        if form.is_valid():
            request.user.delete()
            auth_logout(request)
            return redirect("articles:index")
    else:
        form = PasswordConfirmationForm()
    context = {"form":form}
    return render(request, "accounts/delete.html", context)


@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("articles:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)