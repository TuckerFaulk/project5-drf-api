from django.urls import path
from assigned_to import views

urlpatterns = [
    path('assigned-to/', views.AssignedToList.as_view()),
    path('assigned-to/<int:pk>/', views.AssignedToDetail.as_view()),
]
