from rest_framework import serializers
from .models import Action
from datetime import datetime


class ActionDetailSerializer(serializers.ModelSerializer):

    is_assigned_to = serializers.SerializerMethodField()
    is_overdue = serializers.SerializerMethodField()

    # Source: Code Institutes Django REST Framework Videos
    def get_is_assigned_to(self, obj):
        request = self.context['request']
        return request.user == obj.assigned_to

    def get_is_overdue(self, obj):
        if obj.due_date is not None:
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
        model = Action
        fields = [
            'id', 'action_title', 'category', 'description',
            'assigned_to', 'is_assigned_to', 'created_at', 'updated_at',
            'due_date', 'is_overdue', 'risk_rating', 'image', 'status',
        ]


class ActionSerializer(ActionDetailSerializer):
    """
    Serializer for the action model used in list view
    Status is a read only field so it can not be set to closed
    before it is has already been opened
    """
    status = serializers.ReadOnlyField()
