from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view()),
    path('<int:pk>/', views.ProfilePublicView.as_view())
]
