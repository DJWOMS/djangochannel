from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('entry', views.EntryGroupView)
router.register('comments', views.CommentsEntryGroupView)


urlpatterns = [
    path('', views.GroupListView.as_view(), name="list_groups"),
    path('', include(router.urls)),
    path('create/', views.CreateGroupView.as_view(), name="create_group"),
    path('member/<int:pk>/', views.GroupAddMember.as_view(), name="enter_group"),
    path('<int:pk>/', views.GroupView.as_view(), name="detail_group"),
]
