# Generated by Django 3.2.20 on 2023-11-02 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_delete_newuser1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateField(default=datetime.date(2023, 11, 2)),
        ),
    ]
