from rest_framework import serializers
from .models import TaskComment


class TaskCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = TaskComment
        fields = [
            'id', 'owner', 'task_name', 'created_at', 'updated_at',
            'content', 'is_owner',
        ]


class TaskCommentDetailSerializer(TaskCommentSerializer):
    """
    Serializer for the task Comment model used in Detail view
    Task name is a read only field so that we dont have to set it on each 
    update
    """
    task_name = serializers.ReadOnlyField(source='task_name.id')
