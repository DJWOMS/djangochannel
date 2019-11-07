from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.ListCategoryView.as_view()),
    path('<int:pk>/', views.CourseDetailView.as_view()),
    path('', views.CourseView.as_view())
]
