# Generated by Django 4.2.8 on 2023-12-13 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0010_products_status_alter_loan_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='category',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='img',
        ),
    ]
