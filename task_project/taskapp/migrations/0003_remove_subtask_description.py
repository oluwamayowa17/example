# Generated by Django 3.2.5 on 2024-03-21 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_auto_20240321_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='description',
        ),
    ]
