from rest_framework import serializers
from .models import Action


class ActionSerializer(serializers.ModelSerializer):

    is_assigned_to = serializers.SerializerMethodField()

    # Source: Code Institutes Django REST Framework Videos
    def get_is_assigned_to(self, obj):
        request = self.context['request']
        return request.user == obj.assigned_to

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
        model = Action
        fields = [
            'id', 'action_title', 'category', 'description',
            'assigned_to', 'is_assigned_to', 'created_at', 'updated_at',
            'due_date', 'risk_rating', 'image', 'status',
        ]
