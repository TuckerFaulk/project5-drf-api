from rest_framework import generics, permissions
from .models import TaskComment, ActionComment
from .serializers import TaskCommentSerializer, TaskCommentDetailSerializer, ActionCommentSerializer, ActionCommentDetailSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class TaskCommentList(generics.ListCreateAPIView):
    """
    Lists all user task comments.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer

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
    permission_classes = [IsOwnerOrReadOnly]
    queryset = ActionComment.objects.all()
    serializer_class = ActionCommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ActionCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete user action comments by the comment owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = ActionComment.objects.all()
    serializer_class = ActionCommentDetailSerializer
