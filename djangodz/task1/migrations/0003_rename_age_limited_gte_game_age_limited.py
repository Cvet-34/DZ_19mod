# Generated by Django 5.1.4 on 2024-12-04 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_alter_game_buyer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='age_limited_gte',
            new_name='age_limited',
        ),
    ]
