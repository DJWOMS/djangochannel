from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name="profile"),
    path('edit-avatar/', views.ProfileEditView.as_view(), name="edit-avatar"),

    path('messages/', views.MessagesList.as_view(), name="messages"),
    path('create-message/', views.Rooms.as_view(), name="create_message"),
    path('message/<int:pk>/', views.DetailMessages.as_view(), name="detail_message"),
    path('user/<int:pk>/', views.PublicUserInfo.as_view(), name="public_profile"),
    path('all-users/', views.AllUserProfile.as_view(), name="all_profiles"),
    path('records/<int:pk>/', views.PersonalRecordsList.as_view(), name="personal_records"),
    # path('notes/<int:pk>/', views.PublicPersonalRecordsList.as_view(), name="profile_records"),

    path('user/<int:pk>/add-record/', views.PersonalRecordsCreate.as_view(), name="add_record"),
    path('records-update/<int:pk>/', views.PersonalRecordsUpdate.as_view(), name="update_records"),
    path('record/<int:pk>/', views.PersonalRecordsDetail.as_view(), name="detail_record"),
    path('delete/<int:pk>/', views.PersonalRecordsDelete.as_view(), name="delete_record"),
    path('sorted/', views.SortedPersonalRecords.as_view(), name="sorted_record"),
    path('search-user/', views.SearchUser.as_view(), name="search_user"),
    path('public-records/', views.AllRecordsOfUsers.as_view(), name="public_records"),
    path('edit/', views.PasswordChangeView.as_view(), name="password_edit"),
    # api
    # path('', api_views.MyProfile.as_view()),
    # path('me/', api_views.AboutMe.as_view()),

]
