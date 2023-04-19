from django.db import IntegrityError
from rest_framework import serializers
from .models import AssignedTo


class AssignedToSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    task_name = serializers.SerializerMethodField()
    assigned_to = serializers.SerializerMethodField()

    # Source: Code Institutes Django REST Framework Videos
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Source: https://stackoverflow.com/questions/63130043/how-to-get-field-name-instead-of-foreign-id-in-django
    def get_task_name(self, instance):
        return instance.task_name.task_name

    def get_assigned_to(self, instance):
        return instance.assigned_to.username

    class Meta:
        model = AssignedTo
        fields = [
            'id', 'owner', 'task_name', 'assigned_to',
            'initial_due_date', 'completed_by', 'is_owner',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
