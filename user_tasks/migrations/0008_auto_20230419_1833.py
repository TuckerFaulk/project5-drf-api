# Generated by Django 3.2.18 on 2023-04-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_tasks', '0007_auto_20230419_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='completed_by',
            field=models.CharField(choices=[('User', 'User'), ('Admin', 'Admin')], default='User', max_length=32),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=32),
        ),
    ]
