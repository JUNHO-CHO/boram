from django import forms
from .models import Article, Comment, Tag


class ArticleForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="쉼표로 태그를 구분하세요.")
    class Meta:
        model = Article
        fields = "__all__"
        exclude = ('created_at', 'updated_at', "author")
    def save(self, commit=True):
        instance = super().save(commit=False)
        tags_str = self.cleaned_data['tags']
        if commit:
            instance.save()
            instance.tags.clear()
            for tag_name in tags_str.split(','):
                tag_name = tag_name.strip()
                if tag_name:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    instance.tags.add(tag)
        return instance

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("article", "user")