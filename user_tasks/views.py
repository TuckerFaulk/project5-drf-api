from rest_framework import generics, permissions, filters
from .models import UserTask
from .serializers import UserTaskSerializer
from drf_api.permissions import IsAssignedToOrReadOnly


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
    permission_classes = [IsAssignedToOrReadOnly | permissions.IsAdminUser]
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer
