# Generated by Django 4.2 on 2024-08-20 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gateway',
            old_name='is_enabled',
            new_name='is_active',
        ),
    ]
