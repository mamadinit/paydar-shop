from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Article
from comment.models import ArticleComment
from comment.forms import ArticleCommentCreateForm

# Create your views here.

class ArticleDetailView(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        self.article = get_object_or_404(Article.objects.published(), slug=slug)
		
        print(slug)

        return self.article
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article, slug=slug)
        context['comments'] = ArticleComment.objects.filter(article=article, status='confirmed')
        context['form'] = ArticleCommentCreateForm()
        return context






