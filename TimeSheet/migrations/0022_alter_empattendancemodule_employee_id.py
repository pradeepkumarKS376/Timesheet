# Generated by Django 4.2.9 on 2024-01-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeSheet', '0021_alter_empattendancemodule_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empattendancemodule',
            name='Employee_id',
            field=models.CharField(default=None, max_length=254),
        ),
    ]
