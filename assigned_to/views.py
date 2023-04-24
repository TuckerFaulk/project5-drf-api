from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import AssignedTo
from .serializers import AssignedToSerializer


class AssignedToList(generics.ListCreateAPIView):
    """

    """
    permission_classes = [permissions.IsAdminUser]
    queryset = AssignedTo.objects.all()
    serializer_class = AssignedToSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'task_name',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AssignedToDetail(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    permission_classes = [permissions.IsAdminUser]
    queryset = AssignedTo.objects.all()
    serializer_class = AssignedToSerializer
