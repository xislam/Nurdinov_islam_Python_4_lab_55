from django import forms

from webapp.models import Article, Comment


class ArticleForm(forms.ModelForm):
    tag = forms.CharField(max_length=100, label='Тег', required=False)

    class Meta:
        model = Article
        exclude = ['created_at', 'updated_at', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['created_at', 'updated_at']


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
