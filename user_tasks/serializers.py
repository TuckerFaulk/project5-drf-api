from rest_framework import serializers
from .models import UserTask


class UserTaskSerializer(serializers.ModelSerializer):

    task_name = serializers.ReadOnlyField(source='task_name.task_name')
    completed_by = serializers.ReadOnlyField()
    assigned_to = serializers.ReadOnlyField(
        source='assigned_to.assigned_to.username')
    category = serializers.ReadOnlyField(source='task.category')
    description = serializers.ReadOnlyField(source='task.description')

    class Meta:
        model = UserTask
        fields = [
            'id', 'task_name', 'description', 'category', 'assigned_to',
            'created_at', 'updated_at', 'due_date',
            'action_required', 'action_description', 'completed_by', 'image',
            'status',
        ]
        extra_kwargs = {
            'due_date': {'read_only': True}
        }