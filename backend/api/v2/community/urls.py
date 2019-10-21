from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateGroupView.as_view()),
    path('member/<int:pk>/', views.GroupAddMember.as_view()),


    path('entry/', views.EntryGroupView.as_view()),
    path('entry/<int:pk>/', views.EntryGroupView.as_view()),

    path('<int:pk>/', views.GroupView.as_view()),
    path('', views.GroupListView.as_view()),
]
