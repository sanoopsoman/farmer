# Generated by Django 4.2.8 on 2023-12-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0023_alter_booklandrent_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookvehiclerent',
            name='Status',
            field=models.IntegerField(default=-2013),
            preserve_default=False,
        ),
    ]
