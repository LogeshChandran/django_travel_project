# Generated by Django 4.1.7 on 2023-03-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0007_remove_services_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]