from rest_framework import generics, permissions
from .models import UserTask
from .serializers import UserTaskSerializer


class UserTaskList(generics.ListAPIView):
    """
    No POST method as User Tasks are create from the assignd to singal
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Need to check whether this is the correct class
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer


class UserTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer
