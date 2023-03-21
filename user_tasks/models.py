from django.db import models
from django.contrib.auth.models import User
from master_tasks.models import MasterTask
from assigned_to.models import AssignedTo
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserTask(models.Model):

    status_filter_choices = [
        ("open", "Open"), ("in progress", "In Progress"), ("closed", "Closed")]
    action_by_filter_choices = [("user", "User"), ("admin", "Admin"),]

    task_name = models.ForeignKey(MasterTask, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(AssignedTo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(blank=False)
    action_required = models.BooleanField(default=False)
    action_description = models.TextField(blank=True)
    completed_by = models.CharField(
        max_length=32, choices=action_by_filter_choices, default='user'
    )
    image = models.ImageField(upload_to='images/', blank=True)
    status = models.CharField(
        max_length=32, choices=status_filter_choices, default='open'
    )

    class Meta:
        ordering = ['task_name', 'assigned_to']

    def __str__(self):
        return f"{self.task_name} - {self.assigned_to}"


@receiver(post_save, sender=AssignedTo)
def create_intial_user_task(sender, instance, created, **kwargs):
    if created:
        UserTask.objects.create(
            task_name=instance.task_name,
            assigned_to=instance,
            due_date=instance.initial_due_date,
            completed_by=instance.completed_by,
            )