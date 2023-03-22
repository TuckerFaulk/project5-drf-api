from django.db import models
from django.contrib.auth.models import User
from user_tasks.models import UserTask
from actions.models import Action
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class Comments(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']
        abstract = True

    def __str__(self):
        return self.content


class TaskComment(Comments):
    task_name = models.ForeignKey(UserTask, on_delete=models.CASCADE)


class ActionComment(Comments):
    action_title = models.ForeignKey(Action, on_delete=models.CASCADE)
