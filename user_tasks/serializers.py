from rest_framework import serializers
from .models import UserTask


class UserTaskSerializer(serializers.ModelSerializer):

    task_name = serializers.ReadOnlyField(source='task_name.task_name')
    completed_by = serializers.ReadOnlyField()
    assigned_to = serializers.ReadOnlyField(
        source='assigned_to.assigned_to.username')
    category = serializers.ReadOnlyField(
        source='task_name.category.category_name')
    description = serializers.ReadOnlyField(source='task_name.description')
    frequency = serializers.ReadOnlyField(source='task_name.frequency')

    # Source: Code Institutes Django REST Framework Videos
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger then 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    class Meta:
        model = UserTask
        fields = [
            'id', 'task_name', 'description', 'category', 'assigned_to',
            'created_at', 'updated_at', 'due_date', 'frequency',
            'action_required', 'action_description', 'completed_by', 'image',
            'status',
        ]
        extra_kwargs = {
            'due_date': {'read_only': True}
        }
