from rest_framework import generics, permissions
from .models import UserTask
from .serializers import UserTaskSerializer
from drf_api.permissions import IsAssignedToOrReadOnly


class UserTaskList(generics.ListAPIView):
    """
    No POST method as User Tasks are either created when initially assigned
    or when a user task is closed and the frequency is not 'once'
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Need to check whether this is the correct class
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer


class UserTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    permission_classes = [IsAssignedToOrReadOnly]
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer
