# Generated by Django 2.2.6 on 2020-02-20 16:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LiveTracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livetracking',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 16, 49, 30, 31149, tzinfo=utc)),
        ),
    ]
