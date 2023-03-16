from rest_framework import serializers
from .models import MasterTask


class MasterTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MasterTask
        fields = [
            'id', 'task_name', 'owner', 'created_at', 'updated_at',
            'category', 'description', 'frequency',
        ]
