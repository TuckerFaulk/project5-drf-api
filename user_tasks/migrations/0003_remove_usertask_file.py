# Generated by Django 3.2.18 on 2023-03-21 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_tasks', '0002_rename_action_by_usertask_completed_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertask',
            name='file',
        ),
    ]
