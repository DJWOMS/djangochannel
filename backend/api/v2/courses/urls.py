from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.ListCategoryView.as_view(), name="course_categories"),
    path('<int:pk>/', views.CourseDetailView.as_view(), name="detail_course"),
    path('', views.CourseView.as_view())
]
