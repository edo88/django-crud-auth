# Generated by Django 4.1.1 on 2023-02-21 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_remove_respuesta_requerimiento_task_respuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='respuesta',
        ),
        migrations.AddField(
            model_name='respuesta',
            name='requerimiento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
            preserve_default=False,
        ),
    ]
