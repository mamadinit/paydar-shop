from django.contrib import admin
from django.urls import path
from .views import ProductDetailView

from .views import (
    CartAddItemView, 
    CartDetailView, 
    CartRemoveItemView, 
    OrderCreateView, 
    OrderDetailView,
    CouponApplyView,
    OrderCancelView,
    HomeView,
    SearchView)

app_name = 'shop'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/add/<product_id>/', CartAddItemView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', CartRemoveItemView.as_view(), name='cart_remove'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/cancel/<int:pk>/', OrderCancelView.as_view(), name='order_cancel'),
    path('coupon/<int:order_id>', CouponApplyView.as_view(), name='coupon_apply'),
]


