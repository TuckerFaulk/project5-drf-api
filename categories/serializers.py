from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category Model
    """
    class Meta:
        model = Category
        fields = [
            'id', 'category_name',
        ]
