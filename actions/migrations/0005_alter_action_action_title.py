# Generated by Django 3.2.18 on 2023-03-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0004_alter_action_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='action_title',
            field=models.CharField(max_length=80),
        ),
    ]
