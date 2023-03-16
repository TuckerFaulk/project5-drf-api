from django.db import models
from django.contrib.auth.models import User
from categories.models import Categories


class MasterTask(models.Model):

    frequency_filter_choices = [
        ("once", "Once"),
        ("daily", "Daily"),
        ("weekly", "Weekly"),
        ("monthly", "Monthly"),
        ("biannually", "Biannually"),
        ("annually", "Annually"),
        ]

    task_name = models.CharField(max_length=80, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    frequency = models.CharField(
        max_length=32, choices=frequency_filter_choices, default='once'
    )

    class Meta:
        ordering = ['task_name']

    def __str__(self):
        return f"{self.category} - {self.task_name}"
