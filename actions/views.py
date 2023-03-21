from rest_framework import generics, permissions
from .models import Action
from .serializers import ActionSerializer
from drf_api.permissions import IsAssignedToOrReadOnly


class ActionList(generics.ListCreateAPIView):
    """
    Lists all actions.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an action if it is assigned to the logged in
    user or an admin user is logged in
    """
    permission_classes = [IsAssignedToOrReadOnly | permissions.IsAdminUser]
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
