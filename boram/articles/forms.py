from django import forms
from .models import Article, Comment, Tag


class ArticleForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="쉼표로 태그를 구분하세요.", widget=forms.TextInput(
        attrs={'class': 'my-class col-6', 'placeholder': '쉼표로 태그를 구분하세요.', }))

    class Meta:
        model = Article
        fields = "__all__"
        exclude = ('created_at', 'updated_at', "author",
                   "like_users", "like", "search")
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
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%;'
            }),
            # 'tags': forms.CharField(attrs={
            #     'placeholder': '상품에 대한 설명을 적어주세요.',
            # })
        }
        labels = {
            'title': "상품명",
            'content': "설명",
            'image': "상품 사진"
        }

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

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            hashtags = self.instance.tags.all()
            initial_hashtags = ','.join([f"{hashtag.name}" for hashtag in hashtags])
            self.initial['tags'] = initial_hashtags
            print(initial_hashtags)


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
