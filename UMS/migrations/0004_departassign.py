# Generated by Django 5.0.13 on 2025-03-26 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UMS', '0003_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartAssign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('assign_date', models.DateField()),
                ('position', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UMS.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UMS.faculty')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
