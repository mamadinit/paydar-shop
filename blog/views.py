from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Article

# Create your views here.

class ArticleDetailView(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')







