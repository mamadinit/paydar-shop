from django.contrib import admin
from django.urls import path
from .views import ProductCommentDeleteView, ProductCommentCreateView, ArticleCommentCreateView, ArticleCommentDeleteView


app_name = 'comment'


urlpatterns = [
    path('product-create/<slug>/', ProductCommentCreateView.as_view(), name='product-comment-create'),
    path('product-delete/<pk>/', ProductCommentDeleteView.as_view(), name='product-comment-delete'),

    path('article-create/<slug>/', ArticleCommentCreateView.as_view(), name='article-comment-create'),
    path('article-delete/<pk>/', ArticleCommentDeleteView.as_view(), name='article-comment-delete'),
]

