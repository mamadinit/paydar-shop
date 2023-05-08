from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import SignUpView, VerifyView, CustomLoginView, ResendVerifyView
from .forms import CustomPasswordResetForm

app_name = 'account'


urlpatterns = [
    path('verify/', VerifyView.as_view(), name='verify'),
    path('verify/resend/', ResendVerifyView.as_view(), name='resend'),
]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)