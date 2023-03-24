from rest_framework import generics, permissions, filters
from .models import MasterTask
from .serializers import MasterTaskSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class MasterTaskList(generics.ListCreateAPIView):
    """
    Lists and create actions.
    Permission for admin only.
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = MasterTask.objects.all()
    serializer_class = MasterTaskSerializer
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        'task_name',
        'category__category_name',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MasterTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a master task.
    Permission for admin only - only an admin owner can update or delete
    their own master task.
    """
    permission_classes = [IsOwnerOrReadOnly & permissions.IsAdminUser]
    queryset = MasterTask.objects.all()
    serializer_class = MasterTaskSerializer
