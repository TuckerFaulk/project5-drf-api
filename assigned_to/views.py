from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import AssignedTo
from .serializers import AssignedToSerializer


class AssignedToList(generics.ListCreateAPIView):
    """

    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = AssignedTo.objects.all()
    serializer_class = AssignedToSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AssignedToDetail(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = AssignedTo.objects.all()
    serializer_class = AssignedToSerializer
