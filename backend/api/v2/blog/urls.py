from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="list_post"),
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name="detail_post"),
    # path('categories/', views.CategoriesView.as_view()),
    # path('sort_post/<slug:slug>/', views.SortPostCategory.as_view()),
    # path("search_published/", views.DayWeekMonth.as_view()),
]
