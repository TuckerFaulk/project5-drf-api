from rest_framework import serializers
from .models import MasterTask


class MasterTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    # Source: Code Institutes Django REST Framework Videos
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = MasterTask
        fields = [
            'id', 'task_name', 'owner', 'created_at', 'updated_at',
            'category', 'description', 'frequency', 'is_owner',
        ]
