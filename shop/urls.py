from django.contrib import admin
from django.urls import path
from .views import ProductDetailView

app_name = 'account'


urlpatterns = [
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
]


