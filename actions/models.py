from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from user_tasks.models import UserTask
from django.db.models.signals import post_save
from django.dispatch import receiver


class Action(models.Model):
    """Model for Actions"""
    risk_rating_filter_choices = [
        ("Low", "Low"), ("Medium", "Medium"), ("High", "High")]
    status_filter_choices = [
        ("Open", "Open"), ("Closed", "Closed")]

    action_title = models.CharField(max_length=80)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='action_category')
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='action_assigned_to',
        limit_choices_to={'is_staff': False})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    risk_rating = models.CharField(
        max_length=6, choices=risk_rating_filter_choices, default='Low'
    )
    image = models.ImageField(upload_to='images/', blank=True)
    status = models.CharField(
        max_length=12, choices=status_filter_choices, default='Open'
    )

    class Meta:
        ordering = ['action_title', 'assigned_to']

    def __str__(self):
        return f"{self.action_title} - {self.assigned_to}"


@receiver(post_save, sender=UserTask)
def create_task_action(sender, instance, created, **kwargs):
    """
    Signal to create new action if action-require is true
    when a user task is closed.
    """
    if created is False and instance.status == "Closed" and instance.action_required:

        Action.objects.create(
            action_title=instance.task_name.task_name,
            category=instance.task_name.category,
            description=instance.action_description,
            assigned_to=instance.assigned_to.assigned_to,
        )
