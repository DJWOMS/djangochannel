from django.urls import path
from . import views

urlpatterns = [
    path('add-post/', views.CreatePostView.as_view(), name="add_post"),
    path('comments/', views.CommentsView.as_view(), name="comment"),
    path('comments/<int:pk>/', views.CommentsView.as_view(), name="comment"),
    path('categories/', views.CategoriesView.as_view(), name="list_category"),
    path('<int:pk>/', views.PostDetailView.as_view(), name="detail_post"),
    path('', views.PostListView.as_view(), name="list_post"),
]
