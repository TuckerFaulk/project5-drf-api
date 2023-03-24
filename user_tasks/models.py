from django.db import models
from django.contrib.auth.models import User
from master_tasks.models import MasterTask
from assigned_to.models import AssignedTo
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta


class UserTask(models.Model):

    status_filter_choices = [("open", "Open"), ("closed", "Closed")]
    completed_by_filter_choices = [("user", "User"), ("admin", "Admin"),]

    task_name = models.ForeignKey(
        MasterTask, on_delete=models.CASCADE, related_name='user_task_task_name')
    assigned_to = models.ForeignKey(
        AssignedTo, on_delete=models.CASCADE, related_name='user_task_assigned_to')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(blank=False)
    action_required = models.BooleanField(default=False)
    action_description = models.TextField(blank=True)
    completed_by = models.CharField(
        max_length=32, choices=completed_by_filter_choices, default='user'
    )
    image = models.ImageField(upload_to='images/', blank=True)
    status = models.CharField(
        max_length=32, choices=status_filter_choices, default='open'
    )

    class Meta:
        ordering = ['assigned_to']

    def __str__(self):
        return f"{self.assigned_to}"


@receiver(post_save, sender=AssignedTo)
def create_intial_user_task(sender, instance, created, **kwargs):
    if created:
        UserTask.objects.create(
            task_name=instance.task_name,
            assigned_to=instance,
            due_date=instance.initial_due_date,
            completed_by=instance.completed_by,
        )


@receiver(post_save, sender=UserTask)
def create_repeated_user_task(sender, instance, created, **kwargs):

    # Does this need to be a try/catch(err) to handle any potential errors

    todays_date = datetime.now()

    if created is False and instance.status == "closed" and instance.task_name.frequency != "one off":
        if instance.task_name.frequency == "daily":
            repeated_due_date = todays_date + timedelta(days=1)
        if instance.task_name.frequency == "weekly":
            repeated_due_date = todays_date + timedelta(days=7)
        if instance.task_name.frequency == "monthly":
            repeated_due_date = todays_date + timedelta(days=28)
        if instance.task_name.frequency == "biannually":
            repeated_due_date = todays_date + timedelta(days=182)
        if instance.task_name.frequency == "annually":
            repeated_due_date = todays_date + timedelta(days=365)

        UserTask.objects.create(
            task_name=instance.task_name,
            assigned_to=instance.assigned_to,
            due_date=repeated_due_date,
            completed_by=instance.assigned_to.completed_by,
        )
