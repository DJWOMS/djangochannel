from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('entry', views.EntryGroupView)
router.register('comments', views.CommentsEntryGroupView)


urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.CreateGroupView.as_view()),
    path('member/<int:pk>/', views.GroupAddMember.as_view()),
    path('<int:pk>/', views.GroupView.as_view()),
    # path('', views.GroupListView.as_view()),
]
