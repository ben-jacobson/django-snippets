# Generated by Django 2.1 on 2018-08-12 01:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180812_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2018, 8, 12, 1, 0, 40, 665706, tzinfo=utc), help_text='Date Created'),
        ),
    ]
