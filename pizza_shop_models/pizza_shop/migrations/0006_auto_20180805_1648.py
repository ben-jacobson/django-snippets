# Generated by Django 2.1 on 2018-08-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_shop', '0005_auto_20180805_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topping',
            name='ingredient_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
