from django.db import models
from django.contrib.auth.models import User
from user_tasks.models import UserTask
from actions.models import Action
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=UserTask)
def create_task_status_comment(sender, instance, created, **kwargs):
    if created is False and instance.status == "closed":
        # reference https://stackoverflow.com/questions/4721771/get-current-user-log-in-signal-in-django
        import inspect
        for frame_record in inspect.stack():
            if frame_record[3] == 'get_response':
                request = frame_record[0].f_locals['request']
                break
        else:
            request = None

        TaskComment.objects.create(
            task_name=instance,
            content="Task closed",
            owner=request.user,
            )


@receiver(post_save, sender=Action)
def create_action_status_comment(sender, instance, created, **kwargs):
    if created is False and instance.status == "closed":
        # reference https://stackoverflow.com/questions/4721771/get-current-user-log-in-signal-in-django
        import inspect
        for frame_record in inspect.stack():
            if frame_record[3] == 'get_response':
                request = frame_record[0].f_locals['request']
                break
        else:
            request = None

        ActionComment.objects.create(
            action_title=instance,
            content="Action closed",
            owner=request.user,
            )
