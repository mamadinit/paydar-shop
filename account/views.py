from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView
from .forms import CustomUserCreationForm, VerifyForm
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth import login as auth_login, get_user_model
from pyotp import OTP,HOTP
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic.base import View
from .models import User
from .exceptions import UserNotVerified
from .gateways.sms import send


UserModel = get_user_model()

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class VerifyMixin:
    def user(self):
        try:
            user = UserModel.objects.get(phone=self.request.session['phone'])
            return user
        except UserModel.DoesNotExist:
            print('UserModel.DoesNotExist') 
        except KeyError as e:
            print(e) 

    def hotp(self):
        user = self.user()
        secret = user.otp_secret
        hotp = HOTP(secret)
        return hotp
       
    def otp_code(self):
        otp_code = self.hotp().at(self.user().otp_counter)
        return otp_code



class VerifyView(VerifyMixin, FormView):
    form_class = VerifyForm
    success_url = reverse_lazy('login')
    template_name = 'registration/verify.html'

    def get(self, request, *args, **kwargs):
        if self.user:
            return super().get(self, request, *args, **kwargs)
        else :
            return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        form_otp_code = str(request.POST.get('otp_code'))
        if  self.hotp().verify(form_otp_code, self.user().otp_counter):
            user = self.user()
            user.is_verified = True
            user.save()
            messages.success(self.request,'اکانت شما با موفقیت فعال شد. اکنون وارد شوید !', 'success')
            return super().post(self, request, *args, **kwargs)
        else :
            messages.warning(self.request,'کد وارد شده اشتباه است !')
            return self.form_invalid(self.form_class)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = self.request.session['phone']
        return context

class ResendVerifyView(VerifyMixin, View):
    
    def get(self, request, *args, **kwargs):
        if self.user():
            user = self.user()
            user.otp_counter += 1
            user.save()
            send(user.phone, self.otp_code())
        return HttpResponseRedirect(reverse_lazy('account:verify'))


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get(self, request, *args, **kwargs):
        if 'phone' in self.request.session.keys():
            del self.request.session['phone']
        return super().get(self, request, *args, **kwargs)

    def form_valid(self, form):
        try :
            auth_login(self.request, form.get_user())
        except UserNotVerified:
            pass
        else:
            return HttpResponseRedirect(self.get_success_url())