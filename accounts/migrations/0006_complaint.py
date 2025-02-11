# Generated by Django 4.2.16 on 2024-10-27 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userbiometric'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=100)),
                ('incident_type', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('complaint_details', models.TextField()),
                ('status', models.CharField(max_length=50)),
                ('evidences', models.JSONField(default=list)),
            ],
        ),
    ]
