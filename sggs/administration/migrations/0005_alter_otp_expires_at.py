# Generated by Django 4.2.11 on 2024-05-05 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_customuser_is_librarian_alter_otp_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 6, 52, 12, 667759, tzinfo=datetime.timezone.utc)),
        ),
    ]
