# Generated by Django 4.0.4 on 2022-06-15 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tournament_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='game',
        ),
    ]
