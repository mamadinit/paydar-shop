from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import ProductComment, ArticleComment
from shop.models import Product
from blog.models import Article
from .forms import ProductCommentCreateForm, ArticleCommentCreateForm
# Create your views here.




class ProductCommentDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        slug = self.kwargs.get('slug')
        comment = get_object_or_404(ProductComment, pk=pk, user=request.user)
        comment.delete()
        messages.success(self.request,f'نظر " {comment.content} " به موفقیت حذف شد .', 'success')
        return redirect('dashboard:dashboard-comments')



class ProductCommentCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = ProductCommentCreateForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            slug = self.kwargs.get('slug')
            product = get_object_or_404(Product, slug=self.kwargs.get('slug'))
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
            messages.error(request, 'نظر شما ثبت و در انتظار تایید میباشید . ', 'success')
        else:
            form = ProductCommentCreateForm()

        return redirect('shop:product-detail', product.slug)



class ArticleCommentDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        slug = self.kwargs.get('slug')
        comment = get_object_or_404(ArticleComment, pk=pk, user=request.user)
        comment.delete()
        messages.success(self.request,f'نظر " {comment.content} " به موفقیت حذف شد .', 'success')
        return redirect('dashboard:dashboard-comments')



class ArticleCommentCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = ArticleCommentCreateForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            slug = self.kwargs.get('slug')
            product = get_object_or_404(Product, slug=self.kwargs.get('slug'))
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
            messages.error(request, 'نظر شما ثبت و در انتظار تایید میباشید . ', 'success')
        else:
            form = ArticleCommentCreateForm()

        return redirect('shop:article-detail', product.slug)
