# Generated by Django 4.0.4 on 2022-06-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tournament_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='team',
            field=models.ManyToManyField(blank=True, null=True, to='main.team'),
        ),
    ]