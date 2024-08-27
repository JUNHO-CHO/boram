from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        exclude = ('created_at', 'updated_at', "author")
        widgets = {
            'title': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '상품명을 적어주세요. (50자 이내)',
            'style': 'width: 100%;'
        }),
            'content': forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': '상품에 대한 설명을 적어주세요.',
            'style': 'width: 100%; height: 200px;'
        }),
            'image': forms.FileInput(attrs={
            'class': 'form-control',
            'style': 'width: 100%;'
        }),
    }
        labels = {
            'title': "상품명",
            'content': "설명",
            'image': "상품 사진"
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("article", "user")


class SearchForm(forms.Form):
    q = forms.CharField(
        label='Search',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )