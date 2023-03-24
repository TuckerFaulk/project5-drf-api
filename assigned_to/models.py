from django.db import models
from django.contrib.auth.models import User
from master_tasks.models import MasterTask


class AssignedTo(models.Model):

    completed_by_filter_choices = [("user", "User"), ("admin", "Admin"),]

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assigned_to_owner')
    task_name = models.ForeignKey(MasterTask, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assigned_to_assigned_to')
    initial_due_date = models.DateField(blank=False)
    completed_by = models.CharField(
        max_length=32, choices=completed_by_filter_choices, default='user'
    )

    class Meta:
        ordering = ['task_name', 'assigned_to']
        unique_together = ['owner', 'assigned_to']

    def __str__(self):
        return f'{self.task_name} - {self.assigned_to}'
