from typing import Any, Optional
from django.db import models
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import DetailView

# Create your views here.



class ProductDetailView(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)

        return product