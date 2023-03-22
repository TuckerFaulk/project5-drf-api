from rest_framework import serializers
from .models import AssignedTo


class AssignedToSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    # Source: Code Institutes Django REST Framework Videos
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = AssignedTo
        fields = [
            'id', 'owner', 'task_name', 'assigned_to',
            'initial_due_date', 'completed_by', 'is_owner',
        ]
