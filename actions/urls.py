from django.urls import path
from actions import views

urlpatterns = [
    path('actions/', views.ActionList.as_view()),
    path('actions/<int:pk>/', views.ActionDetail.as_view()),
]
