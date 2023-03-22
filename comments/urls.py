from django.urls import path
from comments import views

urlpatterns = [
    path('task-comments/', views.TaskCommentList.as_view()),
    path('task-comments/<int:pk>/', views.TaskCommentDetail.as_view()),
    path('action-comments/', views.ActionCommentList.as_view()),
    path('action-comments/<int:pk>/', views.ActionCommentDetail.as_view()),
]
