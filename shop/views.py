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
    

class CartAddItemView(LoginRequiredMixin, View):
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
    

class CartRemoveItemView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        print(product)
        cart.remove(product)
        return redirect('shop:cart-detail')


# from django.views import View
# from django.shortcuts import redirect
# from django.utils import timezone
# from django.contrib import messages
# from django.utils.decorators import method_decorator
# from django.views.decorators.http import require_POST
# from .forms import CouponForm
# from .models import Coupon, Order


# class CouponApplyView(View):
#     def post(self, request, order_id):
#         now = timezone.now()
#         form = CouponForm(request.POST)
#         if form.is_valid():
#             code = form.cleaned_data['code']
#             try:
#                 coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gt=now, status=True)
#             except Coupon.DoesNotExist:
#                 messages.error(request, 'کد تخفیف معتبر نیست !', 'danger')
#                 return redirect('orders:detail', order_id)
#             order = Order.objects.get(id=order_id)
#             order.discount = coupon.discount
#             order.save()
#             messages.success(request, 'کد تخفیف اعمال شد')
#             return redirect('orders:detail', order_id)
#         else:
#             messages.error(request, 'دوباره امتحان کنید', 'danger')
#             return redirect('orders:detail', order_id)
