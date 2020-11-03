# Generated by Django 3.1.2 on 2020-11-03 05:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20201101_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='expiry_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2020, 11, 4, 5, 32, 17, 290378, tzinfo=utc)),
        ),
    ]
