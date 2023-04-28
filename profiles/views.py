from django.db.models import Q, Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    No Create (Post) View as profile creation is handled by django signals
    """
    queryset = Profile.objects.annotate(
        user_open_tasks_count=Count(
            'owner__assigned_to_assigned_to__user_task_assigned_to',
            distinct=True, filter=Q(
                owner__assigned_to_assigned_to__user_task_assigned_to__status='Open',
                owner__assigned_to_assigned_to__user_task_assigned_to__completed_by='User')),

        admin_open_tasks_count=Count(
            'owner__assigned_to_assigned_to__user_task_assigned_to',
            distinct=True, filter=Q(
                owner__assigned_to_assigned_to__user_task_assigned_to__status='Open',
                owner__assigned_to_assigned_to__user_task_assigned_to__completed_by='Admin')),

        open_actions_count=Count('owner__action_assigned_to', distinct=True,
                                 filter=Q(owner__action_assigned_to__status='Open')),
    )
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__is_staff',
    ]
    ordering_fields = [
        'user_open_tasks_count',
        'admin_open_tasks_count',
        'open_actions_count',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Detail individual profiles.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        user_open_tasks_count=Count(
            'owner__assigned_to_assigned_to__user_task_assigned_to',
            distinct=True, filter=Q(
                owner__assigned_to_assigned_to__user_task_assigned_to__status='Open',
                owner__assigned_to_assigned_to__user_task_assigned_to__completed_by='User')),

        admin_open_tasks_count=Count(
            'owner__assigned_to_assigned_to__user_task_assigned_to',
            distinct=True, filter=Q(
                owner__assigned_to_assigned_to__user_task_assigned_to__status='Open',
                owner__assigned_to_assigned_to__user_task_assigned_to__completed_by='Admin')),

        open_actions_count=Count('owner__action_assigned_to', distinct=True,
                                 filter=Q(owner__action_assigned_to__status='Open')),
    )
    serializer_class = ProfileSerializer
