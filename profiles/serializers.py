from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_staff = serializers.ReadOnlyField(source='owner.is_staff')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'image',
            'address', 'fire_alarm', 'emergency_lighting',
            'sprinkler_system', 'gas', 'asbestos', 'is_staff',
        ]
