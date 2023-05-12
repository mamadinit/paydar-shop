from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views import View
import datetime
from django.utils import timezone
from django.contrib import messages
from .models import Product, Order, OrderItem, Coupon
from comment.models import Comment
from .utils.cart import Cart
from .forms import Add2CartForm, CouponForm
from account.models import Address
from comment.forms import CommentCreateForm

# Create your views here.



class ProductDetailView(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        
        return product
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        context['comments'] = Comment.objects.filter(product=product, status='confirmed')
        context['form'] = CommentCreateForm()
        return context
    
	
    

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


class OrderDetailView(DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Order, pk=pk)
        return product
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CouponForm
        return context

class OrderCreateView(View):
    def get(self, request):
        print("on OrderCreateView")
        cart = Cart(request)
        delivery_date = datetime.datetime.now() + datetime.timedelta(days=7)
        try:
            order = Order.objects.get(user=request.user, status='awaiting_payment')
            messages.success(request, 'شما یک فاکتور پرداخت نشده دارید لطفا ابتدا پرداخت کنید ', 'warning')
            return redirect('shop:order_detail', order.id)
        except Order.DoesNotExist:
            if cart.get_total_number() == 0:
                messages.success(request, 'سبد خرید خالی است !', 'warning')
                return redirect('shop:cart-detail')
            else:
                try:
                    address = Address.objects.get(user=request.user)
                    new_order = Order.objects.create(user=request.user,
                                                    delivery_date=delivery_date, delivery_address=address)
                    for item in cart:
                        OrderItem.objects.create(order=new_order, product=item['product'], price=item['price'], quantity=item['quantity'])
                    cart.clear() 
                    messages.success(request, f'سفارش {new_order.id} با موفقیت ایجاد شد .', 'info')
                    return redirect('shop:order_detail', new_order.id)
                
                except Address.DoesNotExist:
                    messages.success(request, 'لطفا برای تکمیل سفارش آدرس  وارد کنید .', 'warning')
                    return redirect('address:address-create')


class CouponApplyView(View):
    def post(self, request, order_id):
        now = timezone.now()
        form = CouponForm(request.POST)

        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gt=now, status=True)
            except Coupon.DoesNotExist:
                messages.error(request, 'کد تخفیف معتبر نیست !', 'danger')
                return redirect('shop:order_detail', order_id)
            order = Order.objects.get(id=order_id)
            order.discount = coupon.discount
            order.save()
            messages.error(request, 'کد تخفیف اعمال شد', 'success')
            return redirect('shop:order_detail', order_id)
        else:
            messages.error(request, 'دوباره امتحان کنید', 'danger')
            return redirect('shop:order_detail', order_id)