# Generated by Django 5.0.1 on 2024-01-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeSheet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loginmodule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Name', models.CharField(default=None, max_length=254)),
                ('Account', models.CharField(default=None, max_length=254)),
            ],
            options={
                'db_table': 'Login',
            },
        ),
    ]
