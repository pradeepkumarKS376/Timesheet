# Generated by Django 4.2.9 on 2024-01-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeSheet', '0014_remove_baseclientmodule_task_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseclientmodule',
            name='Task',
        ),
        migrations.AddField(
            model_name='empattendancemodule',
            name='Client_Id',
            field=models.CharField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='empattendancemodule',
            name='Client_Name',
            field=models.CharField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='empattendancemodule',
            name='Task',
            field=models.CharField(choices=[('B', 'Billable'), ('A', 'Admin'), ('H', 'Holiday'), ('L', 'Leave')], default=None, max_length=1),
        ),
    ]