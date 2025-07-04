# Generated by Django 5.0.14 on 2025-05-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UMS', '0012_studentattendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=100)),
                ('port', models.IntegerField(default=80)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
