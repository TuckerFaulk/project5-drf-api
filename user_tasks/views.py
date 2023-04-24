from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import UserTask
from .serializers import UserTaskSerializer
from drf_api.permissions import IsTaskAssignedToOrReadOnly


class UserTaskList(generics.ListAPIView):
    """
    Lists all user tasks.
    No POST method as User Tasks are either created when initially assigned
    or when a user task is closed and the frequency is not 'once'
    No permissions class is required as there is no POST method available
    """
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'task_name',
        'task_name__category',
        'task_name__frequency',
        'assigned_to__assigned_to__profile',
        'completed_by',
        'status',
    ]
    search_fields = [
        'task_name__task_name',
        'task_name__category__category_name',
    ]


class UserTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user task if it is assigned to the logged in
    user or an admin user is logged in. This allows either user to update the
    task if it is to be completed by them.
    """
    permission_classes = [IsTaskAssignedToOrReadOnly | permissions.IsAdminUser]
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer
