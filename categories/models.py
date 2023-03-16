from django.db import models


class Categories(models.Model):
    """Model for Task Categories"""
    category = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category
