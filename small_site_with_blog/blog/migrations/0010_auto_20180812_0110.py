# Generated by Django 2.1 on 2018-08-12 01:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180812_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date Created'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_published',
            field=models.DateTimeField(blank=True, help_text='Date Published', null=True),
        ),
    ]
