from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import DashboardInfoView, DashboardAddressView, DashboardOrderView, DashboardCommentView


app_name = 'dashboard'


urlpatterns = [
    path('', DashboardInfoView.as_view(), name='dashboard-info'),
    path('address/', DashboardAddressView.as_view(), name='dashboard-address'),
    path('oreders/', DashboardOrderView.as_view(), name='dashboard-order'),
    path('comments/', DashboardCommentView.as_view(), name='dashboard-comments'),
]

