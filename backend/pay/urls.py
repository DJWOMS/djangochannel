from django.urls import path
from backend.pay.views import (
    Payment,
    Initialization,
    pending,
    success,
    fail,
    DonateView
)

urlpatterns = [
    path('result/', Payment.as_view(), name='pay-payment'),
    path('redirect/', Initialization.as_view(), name='pay-initialization'),
    path('pending/', pending, name='pay-pending'),
    path('success/', success, name='pay-success'),
    path('fail/', fail, name='pay-fail'),
    path('', Payment.as_view(), name='index'),
    path('donate/', DonateView.as_view(), name="donate-page"),
]
