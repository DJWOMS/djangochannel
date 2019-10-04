from django.urls import path
from . import views

urlpatterns = [
    path('result/', views.Payment.as_view(), name='pay-payment'),
    path('redirect/', views.Initialization.as_view(), name='pay-initialization'),
    path('pending/', views.pending, name='pay-pending'),
    path('success/', views.success, name='pay-success'),
    path('fail/', views.fail, name='pay-fail'),
    path('', views.Payment.as_view(), name='index'),
    path('donate/', views.DonateView.as_view(), name="donate-page"),
]