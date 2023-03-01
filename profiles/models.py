from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_klqque'
    )
    address = models.TextField(blank=True)
    is_admin = models.BooleanField(default=False)

    fire_alarm = models.BooleanField(default=False)
    emergency_lighting = models.BooleanField(default=False)
    sprinkler_system = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    asbestos = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
