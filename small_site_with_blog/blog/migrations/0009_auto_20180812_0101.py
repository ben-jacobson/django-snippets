# Generated by Django 2.1 on 2018-08-12 01:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180812_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now, help_text='Date Created'),
        ),
    ]
