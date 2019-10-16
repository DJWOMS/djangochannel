from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllCourses.as_view(), name="all_courses"),
    path('my-courses/', views.MyCourses.as_view(), name="my_courses"),
    path('task-all/<int:course_id>/', views.MyCourseDetail.as_view(), name="my_course"),
    path('buy-course/<int:pk>/', views.SetUserCoursePay.as_view(), name="buy_course"),
    path('task/<int:pk>/', views.TaskCourse.as_view(), name="task_course"),
    path('<slug:slug>/', views.ListCourse.as_view(), name="courses_list"),
    path('<slug:category>/<slug:slug>/', views.CourseDetail.as_view(), name="courses_detail"),

    # api

    # path('list/', views.CategoryList.as_view()),
    # path('category/', views.CoursesInCategory.as_view()),
    # path('my/', views.MyCourses.as_view()),
    # path('', views.CourseTasks.as_view()),
    # path('task/', views.Tasks.as_view()),
    # path('buy/', views.BuyCourse.as_view()),
    # path('description/', views.CourseDescription.as_view()),
    # path('next/', views.CompletedTasks.as_view()),

]
