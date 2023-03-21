from rest_framework import serializers
from .models import AssignedTo


class AssignedToSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = AssignedTo
        fields = [
            'id', 'owner', 'task_name', 'assigned_to',
            'initial_due_date', 'action_by',
        ]
