# Generated by Django 4.1.1 on 2023-02-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0022_remove_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_ejecutivo',
            field=models.BooleanField(default=False),
        ),
    ]
