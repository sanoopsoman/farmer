# Generated by Django 4.2.8 on 2023-12-12 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0005_loan_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='gallery')),
                ('farmername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farmerapp.farmer')),
            ],
        ),
    ]
