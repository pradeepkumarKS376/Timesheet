# Generated by Django 4.2.9 on 2024-01-08 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TimeSheet', '0010_alter_empattendancemodule_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='empattendancemodule',
            name='Emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TimeSheet.empmodel'),
        ),
    ]
