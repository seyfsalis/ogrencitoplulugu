# Generated by Django 3.1.3 on 2021-01-01 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_forum_tarih'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='tarih',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 1, 21, 51, 42, 908373)),
        ),
    ]