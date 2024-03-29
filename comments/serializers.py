from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import TaskComment, ActionComment


class TaskCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for TaskComment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = TaskComment
        fields = [
            'id', 'owner', 'profile_id', 'profile_image', 'task_name',
            'created_at', 'updated_at', 'content', 'is_owner',
        ]


class TaskCommentDetailSerializer(TaskCommentSerializer):
    """
    Serializer for the task Comment model used in Detail view
    Task name is a read only field so that we dont have to set it on each
    update
    """
    task_name = serializers.ReadOnlyField(source='task_name.id')


class ActionCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for ActionComment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = ActionComment
        fields = [
            'id', 'owner', 'profile_id', 'profile_image', 'action_title',
            'created_at', 'updated_at', 'content', 'is_owner',
        ]


class ActionCommentDetailSerializer(ActionCommentSerializer):
    """
    Serializer for the Action Comment model used in Detail view
    Action Title is a read only field so that we dont have to set it on each
    update
    """
    action_title = serializers.ReadOnlyField(source='action_title.id')
