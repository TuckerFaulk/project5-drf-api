from django.db import IntegrityError
from rest_framework import serializers
from .models import AssignedTo


class AssignedToSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    # Source: Code Institutes Django REST Framework Videos
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Source: https://stackoverflow.com/questions/52491330/how-to-get-foreignkey-field-name-instead-of-id-in-django-rest-framework
    def to_representation(self, instance):
        rep = super(AssignedToSerializer, self).to_representation(instance)
        rep['assigned_to'] = instance.assigned_to.username
        rep['task_name'] = instance.task_name.task_name
        return rep

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
