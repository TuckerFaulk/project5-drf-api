from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import TaskComment, ActionComment
from .serializers import TaskCommentSerializer, TaskCommentDetailSerializer, ActionCommentSerializer, ActionCommentDetailSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class TaskCommentList(generics.ListCreateAPIView):
    """
    Lists all user task comments.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task_name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete user task comments by the comment owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentDetailSerializer


class ActionCommentList(generics.ListCreateAPIView):
    """
    Lists all user action comments.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ActionComment.objects.all()
    serializer_class = ActionCommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['action_title']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ActionCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete user action comments by the comment owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = ActionComment.objects.all()
    serializer_class = ActionCommentDetailSerializer
