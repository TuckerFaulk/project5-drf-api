# Generated by Django 3.2.18 on 2023-03-16 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_tasks', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_name']},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='category_name',
        ),
    ]
