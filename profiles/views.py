from django.db.models import Q, Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    No Create (Post) View as profile creation is handled by django signals
    """
    queryset = Profile.objects.annotate(
        open_tasks_count=Count(
            'owner__assigned_to_assigned_to__user_task_assigned_to',
            distinct=True, filter=Q(
                owner__assigned_to_assigned_to__user_task_assigned_to__status='open')),
        open_actions_count=Count('owner__action_assigned_to', distinct=True,
                                 filter=Q(owner__action_assigned_to__status='open')),
    )
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'open_tasks_count',
        'open_actions_count',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Detail individual profiles
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
