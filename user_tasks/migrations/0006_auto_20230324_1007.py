# Generated by Django 3.2.18 on 2023-03-24 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assigned_to', '0003_auto_20230324_1007'),
        ('master_tasks', '0001_initial'),
        ('user_tasks', '0005_alter_usertask_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_task_assigned_to', to='assigned_to.assignedto'),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='task_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_task_task_name', to='master_tasks.mastertask'),
        ),
    ]