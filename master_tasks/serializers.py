from rest_framework import serializers
from .models import MasterTask


class MasterTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    # Source: Code Institutes Django REST Framework Videos
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Source: https://stackoverflow.com/questions/63130043/how-to-get-field-name-instead-of-foreign-id-in-django
    def get_category(self, instance):
        return instance.category.category_name

    class Meta:
        model = MasterTask
        fields = [
            'id', 'task_name', 'owner', 'is_owner', 'created_at',
            'updated_at', 'category', 'description', 'frequency', 
        ]
