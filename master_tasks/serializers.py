from rest_framework import serializers
from .models import MasterTask


class MasterTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    # Source: Code Institutes Django REST Framework Videos
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Source: https://stackoverflow.com/questions/52491330/how-to-get-foreignkey-field-name-instead-of-id-in-django-rest-framework
    def to_representation(self, instance):
        rep = super(MasterTaskSerializer, self).to_representation(instance)
        rep['category'] = instance.category.category_name
        return rep

    class Meta:
        model = MasterTask
        fields = [
            'id', 'task_name', 'owner', 'is_owner', 'created_at',
            'updated_at', 'category', 'description', 'frequency', 
        ]
