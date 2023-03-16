from django.urls import path
from master_tasks import views

urlpatterns = [
    path('master-tasks/', views.MasterTaskList.as_view()),
]
