from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_staff = serializers.ReadOnlyField(source='owner.is_staff')
    is_owner = serializers.SerializerMethodField()

    user_open_tasks_count = serializers.ReadOnlyField()
    admin_open_tasks_count = serializers.ReadOnlyField()
    open_actions_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'is_owner', 'created_at', 'updated_at', 'image',
            'is_staff', 'user_open_tasks_count', 'admin_open_tasks_count',
            'open_actions_count',
        ]
