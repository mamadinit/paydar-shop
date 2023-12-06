from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView, ListView, View
from django.db.models import Q
import datetime
from django.utils import timezone
from django.contrib import messages
from .models import Product, Order, OrderItem, Coupon
from comment.models import ProductComment
from .utils.cart import Cart
from .forms import Add2CartForm, CouponForm
from account.models import Address
from comment.forms import ProductCommentCreateForm
from blog.models import Article

# Create your views here.

class HomeView(TemplateView):
    template_name = 'shop/home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        
        context['articles'] = Article.objects.published()

        return context


class ProductDetailView(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        
        return product
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        context['comments'] = ProductComment.objects.filter(product=product, status='confirmed')
        context['form'] = ProductCommentCreateForm()
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



class OrderCancelView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk, user=request.user)
        order.status = 'canceled'
        order.save()
        messages.success(self.request, f'سفارش با کد {order.pk} با موفقیت لغو شد .', 'success')
        return redirect('dashboard:dashboard-order')
    

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
        

class SearchView(ListView):
    template_name = 'shop/search.html'

    def get_queryset(self):
        query = self.request.GET.get('query')

        return Product.objects.filter(Q(description__icontains=query) | Q(title__icontains=query))	
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['query'] = self.request.GET.get('query')

        return context