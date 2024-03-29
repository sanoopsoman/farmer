# Generated by Django 4.2.8 on 2023-12-15 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0013_alter_feedback_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30, null=True)),
                ('duration', models.CharField(max_length=30, null=True)),
                ('amount', models.IntegerField()),
                ('techid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmerapp.farmtech')),
            ],
        ),
        migrations.CreateModel(
            name='Lands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50, null=True)),
                ('duration', models.CharField(max_length=50, null=True)),
                ('amount', models.IntegerField()),
                ('techid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmerapp.farmtech')),
            ],
        ),
    ]
