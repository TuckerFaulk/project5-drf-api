# Generated by Django 3.2.18 on 2023-04-26 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_tasks', '0008_auto_20230419_1833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertask',
            options={'ordering': ['due_date']},
        ),
    ]
