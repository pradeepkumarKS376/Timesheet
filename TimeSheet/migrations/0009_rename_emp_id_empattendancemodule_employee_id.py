# Generated by Django 4.2.9 on 2024-01-07 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeSheet', '0008_empattendancemodule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empattendancemodule',
            old_name='Emp_id',
            new_name='Employee_id',
        ),
    ]
