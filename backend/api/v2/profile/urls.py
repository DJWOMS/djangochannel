from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PublicProfileView.as_view()),
    path('', views.ProfileView.as_view()),
]
