# Generated by Django 4.2.8 on 2023-12-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0014_vehicle_lands'),
    ]

    operations = [
        migrations.AddField(
            model_name='lands',
            name='img',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='img',
            field=models.ImageField(default=-2013, upload_to='gallery'),
            preserve_default=False,
        ),
    ]