from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.messages.views import SuccessMessageMixin
from account.models import User, Address
from account.forms import AddressUpdateForm
from shop.models import Order
from comment.models import Comment
from .forms import DashboardInfoForm
from comment.forms import CommentUpdateForm

# Create your views here.




class DashboardInfoView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'dashboard/dashboard-info.html'
    form_class = DashboardInfoForm
    success_url = reverse_lazy('dashboard:dashboard-info')
    success_message = 'اطلاعات حساب کاربری با موفقیت ویرایش شد .'


    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


    def get_form_kwargs(self):
        kwargs = super(DashboardInfoView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class DashboardAddressView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Address
    template_name = 'dashboard/dashboard-address.html'
    form_class = AddressUpdateForm
    success_url = reverse_lazy('dashboard:dashboard-address')
    success_message = "آدرس با موفقیت ویرایش شد ."

    def get_object(self):

        return self.model.objects.filter(user=self.request.user).first()    
    
    def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)
    

class DashboardOrderView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/dashboard-orders.html'

    def get_queryset(self):
        return Order.objects.get_orders_list(user=self.request.user)
    
                                        


class DashboardCommentView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/dashboard-comments.html'

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)