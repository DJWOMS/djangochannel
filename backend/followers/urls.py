from django.urls import path
from . import views

urlpatterns = [

    path('', views.AllFriends.as_view(), name="all_friends"),
    path('followers/', views.AllFollowers.as_view(), name="all_followers"),
    path('add/<int:pk>/', views.AddFollow.as_view(), name="add_friends"),
    path('delete/<int:pk>/', views.RemoveFriends.as_view(), name="delete_friends"),
    path('cancel/<int:pk>/', views.RemoveFriends.as_view(), name="cancel_petition"),
    path('request/', views.FriendRequests.as_view(), name="request_friends"),
    path('friend-confirm/<int:pk>/', views.FriendConfirm.as_view(), name="accept_friendship_in_prof"),
    path('accept/<int:pk>/', views.AddFriends.as_view(), name="accept_friendship"),
    path('not-create/<int:pk>/', views.NotAddFriends.as_view(), name="not_create"),

]
