from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, VerifyView, CustomLoginView, ResendVerifyView
from .forms import CustomPasswordResetForm

app_name = 'account'


urlpatterns = [
    path('verify/', VerifyView.as_view(), name='verify'),
    path('verify/resend/', ResendVerifyView.as_view(), name='resend'),
]

