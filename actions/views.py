from rest_framework import generics, permissions, filters
from .models import Action
from .serializers import ActionSerializer, ActionDetailSerializer
from drf_api.permissions import IsAssignedToOrReadOnly


class ActionList(generics.ListCreateAPIView):
    """
    Lists all actions.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        'action_title',
        'category__category_name',
    ]


class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an action if it is assigned to the logged in
    user or an admin user is logged in
    """
    permission_classes = [IsAssignedToOrReadOnly | permissions.IsAdminUser]
    queryset = Action.objects.all()
    serializer_class = ActionDetailSerializer
