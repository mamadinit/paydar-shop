
from django import forms
from .models import ProductComment, ArticleComment




class ProductCommentCreateForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('content',)
            



class ArticleCommentCreateForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('content',)
            