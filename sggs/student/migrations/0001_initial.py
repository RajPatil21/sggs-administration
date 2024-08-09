# Generated by Django 4.2.11 on 2024-05-05 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administration', '0005_alter_otp_expires_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_edited',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=20)),
                ('year', models.IntegerField(default=2000)),
                ('roll_number', models.CharField(default='', max_length=20)),
                ('date_of_birth', models.DateField(default='2000-01-01')),
                ('address', models.TextField(default='')),
                ('contact_number', models.CharField(default='', max_length=15)),
                ('department', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_edited_department', to='administration.department')),
                ('semester', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_edited_semester', to='administration.semester')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_edited_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fee_edited',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_1_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year_2_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year_3_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year_4_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fee_edited', to='administration.student')),
            ],
        ),
    ]
