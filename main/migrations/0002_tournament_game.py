# Generated by Django 4.0.4 on 2022-06-14 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.game'),
            preserve_default=False,
        ),
    ]
