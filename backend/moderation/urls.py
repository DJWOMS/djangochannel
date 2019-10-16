from django.urls import path
from moderation import views

urlpatterns = [
    path('', views.AboutModerator.as_view()),
    path('ban/', views.BanUser.as_view()),
]
