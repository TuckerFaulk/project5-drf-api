# Generated by Django 3.2.18 on 2023-03-24 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assigned_to', '0003_auto_20230324_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedto',
            name='assigned_to',
            field=models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to_assigned_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
