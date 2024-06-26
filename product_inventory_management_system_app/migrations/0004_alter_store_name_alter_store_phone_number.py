# Generated by Django 4.2.11 on 2024-04-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_inventory_management_system_app', '0003_alter_brand_founded_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
