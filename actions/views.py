from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Action
from .serializers import ActionSerializer, ActionDetailSerializer
from drf_api.permissions import IsActionAssignedToOrReadOnly


class ActionList(generics.ListCreateAPIView):
    """
    Lists all actions.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'assigned_to__profile',
        'category',
        'risk_rating',
        'status',
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
    permission_classes = [IsActionAssignedToOrReadOnly | permissions.IsAdminUser]
    queryset = Action.objects.all()
    serializer_class = ActionDetailSerializer
