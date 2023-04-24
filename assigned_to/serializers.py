from django.db import IntegrityError
from rest_framework import serializers
from .models import AssignedTo


class AssignedToSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    assigned_to_username = serializers.ReadOnlyField(
        source='assigned_to.username')
    task_name_title = serializers.ReadOnlyField(source='task_name.task_name')
    is_owner = serializers.SerializerMethodField()

    # Source: Code Institutes Django REST Framework Videos
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = AssignedTo
        fields = [
            'id', 'owner', 'task_name', 'task_name_title', 'assigned_to',
            'assigned_to_username', 'initial_due_date', 'completed_by',
            'is_owner',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
