# Generated by Django 3.1.3 on 2021-01-03 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeri', '0003_auto_20210103_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeri',
            name='tarih',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 3, 16, 56, 17, 923562)),
        ),
    ]
