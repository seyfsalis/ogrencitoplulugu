# Generated by Django 3.1.3 on 2021-01-01 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20210101_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='tarih',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 1, 21, 54, 0, 219927)),
        ),
    ]
