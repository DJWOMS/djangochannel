from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.ListTests.as_view(), name="dc-tests"),
    path('<int:pk>/', views.DetailTest.as_view(), name="dc-test-detail"),


    # api
#     path('categories/', api_views.AllCategories.as_view()),
#     path('tests/', api_views.TestsInCategory.as_view()),
#     path('questions/', api_views.QuestionsInTest.as_view()),
#     path('answers/', api_views.AnswersInQuestion.as_view()),
#     path('complete/', api_views.CompleteQuestion.as_view()),
]
