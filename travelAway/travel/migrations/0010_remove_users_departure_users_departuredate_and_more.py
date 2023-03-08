# Generated by Django 4.1.7 on 2023-03-08 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_alter_services_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='departure',
        ),
        migrations.AddField(
            model_name='users',
            name='departuredate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='users',
            name='departuretime',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AddField(
            model_name='users',
            name='returntime',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='users',
            name='returndate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]