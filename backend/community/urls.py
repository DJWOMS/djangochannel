from django.urls import path

from . import views

urlpatterns = [
    path("", views.GroupList.as_view(), name="all_groups"),
    path("detail/<int:pk>/", views.GroupDetail.as_view(), name="detail_groups"),
    path("create/", views.CreateGroup.as_view(), name="create_group"),
    path("edit/<int:pk>/", views.EditGroup.as_view(), name="edit_group"),
    path("delete/<int:pk>/", views.RemoveGroup.as_view(), name="delete_group"),
    path("add-record/<int:pk>/", views.CreateRecordGroup.as_view(), name="add_news"),
    path("edit-record/<int:pk>/", views.EditRecordGroup.as_view(), name="edit_record"),
    path(
        "delete-record/<int:pk>/",
        views.RemoveRecordGroup.as_view(),
        name="delete_record",
    ),
    path("add-link/<int:pk>/", views.CreateLinkGroup.as_view(), name="add_link"),
    path("enter/<int:pk>/", views.EnterGroup.as_view(), name="enter_group"),
]
