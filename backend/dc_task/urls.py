from django.urls import path
from . import views

urlpatterns = [
    path('', views.DCTaskList.as_view(), name="dc_task_all"),
    path('specialization/', views.Specialization.as_view(), name="special"),
    path('add-specialization/<int:pk>/', views.AddSpecialUser.as_view(), name="add_spec"),
    path('<slug:category>/<slug:slug>/', views.DCTaskDetail.as_view(), name="dc_task_detail"),
]
