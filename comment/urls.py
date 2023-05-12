from django.contrib import admin
from django.urls import path
from .views import CommentDeleteView, CommentCreateView


app_name = 'comment'


urlpatterns = [
    path('create/<slug>/', CommentCreateView.as_view(), name='comment-create'),
    path('delete/<pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]

