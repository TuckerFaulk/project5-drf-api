from rest_framework import generics, permissions
from .models import AssignedTo
from .serializers import AssignedToSerializer


class AssignedToList(generics.ListCreateAPIView):
    """

    """
    permission_classes = [permissions.IsAdminUser]
    queryset = AssignedTo.objects.all()
    serializer_class = AssignedToSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AssignedToDetail(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    permission_classes = [permissions.IsAdminUser]
    queryset = AssignedTo.objects.all()
    serializer_class = AssignedToSerializer
