from rest_framework import serializers
from .models import Action


class ActionSerializer(serializers.ModelSerializer):

    assigned_to = serializers.ReadOnlyField(source='assigned_to.username')

    class Meta:
        model = Action
        fields = [
            'id', 'action_title', 'category', 'description',
            'assigned_to', 'created_at', 'updated_at', 'due_date',
            'risk_rating', 'image', 'status',
        ]
