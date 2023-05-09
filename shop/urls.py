from django.contrib import admin
from django.urls import path
from .views import ProductDetailView

from .views import CartAddView, CartDetailView

app_name = 'shop'


urlpatterns = [
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/add/<product_id>/', CartAddView.as_view(), name='cart_add'),
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
]


