from rest_framework import serializers
from .models import UserTask
from datetime import datetime, timedelta


class UserTaskSerializer(serializers.ModelSerializer):

    task_name = serializers.ReadOnlyField(source='task_name.task_name')
    completed_by = serializers.ReadOnlyField()
    assigned_to = serializers.ReadOnlyField(
        source='assigned_to.assigned_to.username')
    is_assigned_to = serializers.SerializerMethodField()
    is_overdue = serializers.SerializerMethodField()
    category = serializers.ReadOnlyField(
        source='task_name.category.category_name')
    description = serializers.ReadOnlyField(source='task_name.description')
    frequency = serializers.ReadOnlyField(source='task_name.frequency')

    # Source: Code Institutes Django REST Framework Videos
    def get_is_assigned_to(self, obj):
        request = self.context['request']
        return request.user == obj.assigned_to.assigned_to

    def get_is_overdue(self, obj):
        request = self.context['request']
        todays_date = datetime.now().date()
        return todays_date > obj.due_date

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
            'is_assigned_to', 'created_at', 'updated_at', 'due_date',
            'is_overdue', 'frequency', 'action_required',
            'action_description', 'completed_by', 'image', 'status',
            'overdue_tasks_count',
        ]
        extra_kwargs = {
            'due_date': {'read_only': True}
        }
