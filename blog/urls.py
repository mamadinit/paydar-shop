from django.contrib import admin
from django.urls import path
from .views import  ArticleDetailView

app_name = 'blog'

urlpatterns = [
    # path('', ArticleListView.as_view(), name='article-list'),
    path('<slug>/', ArticleDetailView.as_view(), name='article-detail'),
    # path('article/preview/<slug:slug>/', ArticlePreviewView.as_view(), name="article-preview"),
    # path('search/', SearchListView.as_view(), name='search'),
    # path('author/<slug:username>/', AuthorListView.as_view(), name="author"),
    # path('category/<slug:slug>', CategoryListView.as_view(), name="category"),
    
]