# Generated by Django 4.2 on 2023-04-17 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 15, 42, 45, 181717, tzinfo=datetime.timezone.utc)),
        ),
    ]
