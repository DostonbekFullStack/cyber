# Generated by Django 4.0 on 2022-06-15 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.game'),
            preserve_default=False,
        ),
    ]
