from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroupListView.as_view()),
    path('create/', views.CreateGroupView.as_view()),
    path('add-member/<int:pk>/', views.GroupAddMember.as_view()),
    path('group/<int:pk>/', views.GroupView.as_view()),

    path('entry/', views.EntryGroupView.as_view()),
    path('entry/<int:pk>/', views.EntryGroupView.as_view()),
]
