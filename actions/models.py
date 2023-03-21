from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from user_tasks.models import UserTask
from django.db.models.signals import post_save
from django.dispatch import receiver


class Action(models.Model):

    risk_rating_filter_choices = [
        ("low", "Low"), ("medium", "Medium"), ("high", "High"),]
    status_filter_choices = [
        ("open", "Open"), ("in progress", "In Progress"), ("closed", "Closed")]

    action_title = models.CharField(max_length=80, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    risk_rating = models.CharField(
        max_length=6, choices=risk_rating_filter_choices, default='low'
    )
    image = models.ImageField(upload_to='images/', blank=True)
    status = models.CharField(
        max_length=12, choices=status_filter_choices, default='open'
    )

    class Meta:
        ordering = ['action_title', 'assigned_to']

    def __str__(self):
        return f"{self.action_title} - {self.assigned_to}"


@receiver(post_save, sender=UserTask)
def create_task_action(sender, instance, created, **kwargs):
    if created is False and instance.status == "closed" and instance.action_required:

        Action.objects.create(
            action_title=instance.task_name.task_name,
            category=instance.task_name.category,
            description=instance.action_description,
            assigned_to=instance.assigned_to.assigned_to,
        )