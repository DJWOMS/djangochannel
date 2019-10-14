from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroupListView.as_view()),
    path('create/', views.CreateGroupView.as_view())
]
