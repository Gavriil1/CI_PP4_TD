# Generated by Django 3.2.20 on 2023-11-05 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_task_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateField(default=datetime.date(2023, 11, 5)),
        ),
    ]
