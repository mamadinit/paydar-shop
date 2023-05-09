from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import DashboardInfoView, AddressUpdateView


app_name = 'dashboard'


urlpatterns = [
    path('', DashboardInfoView.as_view(), name='dashboard-info'),
    path('address/', AddressUpdateView.as_view(), name='dashboard-address'),
]

