from django.urls import path
from backend.blog import views

urlpatterns = [
    # api urls
    # path("categories/", api_views.CategoriesList.as_view()),
    # path("post-list/", api_views.PostList.as_view()),
    # path("post-single/", api_views.PostSingle.as_view()),

    # default urls
    path("search/", views.SearchPost.as_view(), name="search"),
    path("published/", views.DayWeekMonth.as_view(), name="sorted"),
    # path("", views.SearchSpy.as_view(), name="search"),

    path("post/<int:pk>/comment-create/", views.CommentCreate.as_view(), name="comments_create"),
    path("post/<int:pk>/comment-update/", views.EditComment.as_view(), name="comment_update"),
    path("comment/<int:pk>/", views.AnswerComment.as_view(), name="answer_comment"),
    path("delete/<int:pk>/", views.DeleteComment.as_view(), name="delete_comment"),
    path("user-post/", views.AddUserPost.as_view(), name="user_post"),
    path("tag/<slug:tag>/", views.PostList.as_view(), name="tag_post"),
    path("<slug:category>/", views.PostList.as_view(), name="category"),
    path("<slug:category>/<slug:slug>/", views.SinglePost.as_view(), name="single_post"),
    path("", views.PostList.as_view(), name="blog"),
]
