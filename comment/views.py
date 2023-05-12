from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Comment
from shop.models import Product
from .forms import CommentCreateForm
# Create your views here.




class CommentDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        slug = self.kwargs.get('slug')
        comment = get_object_or_404(Comment, pk=pk, user=request.user)
        comment.delete()
        messages.success(self.request,f'نظر " {comment.content} " به موفقیت حذف شد .', 'success')
        return redirect('dashboard:dashboard-comments')



class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = CommentCreateForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            slug = self.kwargs.get('slug')
            product = get_object_or_404(Product, slug=self.kwargs.get('slug'))
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
            messages.error(request, 'نظر شما ثبت و در انتظار تایید میباشید . ', 'success')
        else:
            form = CommentCreateForm()

        return redirect('shop:product-detail', product.slug)
