from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_staff = serializers.ReadOnlyField(source='owner.is_staff')

    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'image',
            'address', 'fire_alarm', 'emergency_lighting',
            'sprinkler_system', 'gas', 'asbestos', 'is_staff',
            'is_owner',
        ]
