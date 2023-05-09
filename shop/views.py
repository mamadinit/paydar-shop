from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views import View
from .models import Product
from .utils.cart import Cart
from .forms import Add2CartForm

# Create your views here.



class ProductDetailView(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)

        return product
    

class CartAddView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = Add2CartForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cart.add(product=product, quantity=data['quantity'])
        return redirect('shop:cart-detail')

class CartDetailView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'shop/detail-cart.html', {'cart': cart})