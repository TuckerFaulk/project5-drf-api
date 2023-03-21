from django.urls import path
from user_tasks import views

urlpatterns = [
    path('user-tasks/', views.UserTaskList.as_view()),
    path('user-tasks/<int:pk>/', views.UserTaskDetail.as_view()),
]
