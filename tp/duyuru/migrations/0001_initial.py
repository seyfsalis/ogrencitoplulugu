# Generated by Django 3.1.3 on 2020-11-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duyuru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=150)),
                ('icerik', models.TextField()),
                ('tarih', models.DateTimeField()),
            ],
        ),
    ]
