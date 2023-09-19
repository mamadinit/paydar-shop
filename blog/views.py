from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Article

# Create your views here.

class ArticleDetailView(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        self.article = get_object_or_404(Article.objects.published(), slug=slug)
		
        print(slug)

        return self.article







