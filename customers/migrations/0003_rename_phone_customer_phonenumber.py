# Generated by Django 5.0.1 on 2024-02-09 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='phonenumber',
        ),
    ]
