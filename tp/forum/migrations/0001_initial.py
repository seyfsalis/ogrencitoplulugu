# Generated by Django 3.1.3 on 2020-12-11 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=99)),
                ('icerik', models.TextField()),
                ('grup_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='grup.grup')),
                ('kullanici_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
