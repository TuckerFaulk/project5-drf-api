from rest_framework import generics, permissions
from .models import MasterTask
from .serializers import MasterTaskSerializer


class MasterTaskList(generics.ListCreateAPIView):
    """
    Lists and create actions.
    Permission for admin only.
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = MasterTask.objects.all()
    serializer_class = MasterTaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MasterTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a master task.
    Permission for admin only.
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = MasterTask.objects.all()
    serializer_class = MasterTaskSerializer
