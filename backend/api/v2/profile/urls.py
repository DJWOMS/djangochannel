from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PublicProfileView.as_view(), name="public_profile"),
    path('', views.ProfileView.as_view(), name="profile"),
]
