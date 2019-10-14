from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseView.as_view())
]
