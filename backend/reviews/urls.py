from django.urls import path
from backend.reviews import views

urlpatterns = [
    path('', views.ListReviews.as_view(), name="list_review"),
    path('add/', views.AddReview.as_view(), name="add_review")
    # api
    # path('add/', views.AddReview.as_view()),
    # path('all/', views.AllReviews.as_view()),
    # path('moderated/', views.ModeratedReviews.as_view()),
    # path('not_moderated/', views.NotModeratedReviews.as_view()),
]
