from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    # username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control'}))
    # password = forms.CharField(
    #     label=_("Password"),
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-control'}),
    # )
    class Meta:
        model = Article
        fields = "__all__"
        exclude = ('created_at', 'updated_at', "author", "like_users")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("article", "user")