from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    # path('detail/<int:pk>/', views.PostDetail.as_view()),
    # path('sort_category/', views.SortCategory.as_view()),
    # path('sort_post/<slug:slug>/', views.SortPostCategory.as_view()),
    # path("search_published/", views.DayWeekMonth.as_view()),
]
