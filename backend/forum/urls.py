from django.urls import path
# from backend.forum import api_views
from backend.forum import views

urlpatterns = [
    path('', views.Sections.as_view(), name="sections"),
    path('section/<slug:slug>/', views.TopicsList.as_view(), name="topic-list"),
    path('section/<slug:section>/<int:pk>/', views.TopicDetail.as_view(), name="topic-detail"),
    path('message/<slug:section>/<int:pk>/', views.MessageCreate.as_view(), name="message_create"),
    path('section/<slug:section>/<int:pk>/edit/<int:edit>/', views.EditMessages.as_view(), name="message_edit"),
    path('section/<slug:section>/<int:pk>/edit-topic/', views.EditTopic.as_view(), name="topic_edit"),
    path('create-topic/', views.CreateTopic.as_view(), name="created_topic"),
#section/<slug:section>/<int:pk>/
    # api urls
    # path('', api_views.Categories.as_view()),
    #
    # path('sections/', api_views.Sections.as_view()),
    #
    # path('topic/', api_views.ReadAndCreateTopics.as_view()),
    # # path('topic/create/', api_views.CreateTopic.as_view()),
    # path('topic/change/', api_views.ChangeTopics.as_view()),
    # path('topic/my/', api_views.MyTopics.as_view()),
    # path('topic/comments/', api_views.CountMessages.as_view()),
    # path('topic/not_moderated/', api_views.NotModeratedTopics.as_view()),
    # path('topic/moderate/', api_views.ModerateTopics.as_view()),
    # path('topic/new/', api_views.NewTopics.as_view()),
    #
    # path('comments/', api_views.ReadAndCreateMessages.as_view()),
    # path('comments/change/', api_views.ChangeMessages.as_view()),
    # path('comments/my/', api_views.MyMessages.as_view()),
    # path('comments/not_moderated/', api_views.NotModeratedMessages.as_view()),
    # path('comments/new/', api_views.NewMessages.as_view()),

    # path('ban/minimal/', api_views.MinimalBan.as_view()),
    # path('ban/maximal/', api_views.MaximalBan.as_view()),

    # path('search/', api_views.SearchTopics.as_view()),

    # path('comments/add/', api_views.CreateMessage.as_view()),

]
