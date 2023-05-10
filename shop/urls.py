from django.contrib import admin
from django.urls import path
from .views import ProductDetailView

from .views import CartAddItemView, CartDetailView, CartRemoveItemView

app_name = 'shop'


urlpatterns = [
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/add/<product_id>/', CartAddItemView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', CartRemoveItemView.as_view(), name='cart_remove'),
]


