# Generated by Django 3.1.2 on 2020-10-26 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shippingaddress_extra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='extra',
        ),
    ]
