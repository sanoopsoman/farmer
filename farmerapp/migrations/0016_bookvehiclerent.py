# Generated by Django 4.2.8 on 2023-12-19 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0015_lands_img_vehicle_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookvehiclerent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startingdate', models.DateField()),
                ('endingdate', models.DateField()),
                ('totalamount', models.CharField(max_length=20, null=True)),
                ('fid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farmerapp.farmer')),
                ('techid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farmerapp.farmtech')),
                ('vid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farmerapp.vehicle')),
            ],
        ),
    ]
