# Generated by Django 4.2.11 on 2024-05-13 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0015_alter_otp_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 13, 9, 19, 31, 577143, tzinfo=datetime.timezone.utc)),
        ),
    ]