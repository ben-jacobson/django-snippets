# Generated by Django 2.1 on 2018-09-01 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0004_auto_20180901_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='slug',
            field=models.SlugField(max_length=120, unique=True),
        ),
    ]