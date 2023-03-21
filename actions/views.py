from rest_framework import generics, permissions
from .models import Action
from .serializers import ActionSerializer


class ActionList(generics.ListCreateAPIView):
    """

    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)


class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    permission_classes = [permissions.IsAdminUser]  # Change IsAssignedToOrReadOnly
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
