# Generated by Django 2.1 on 2018-08-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='base_type',
            field=models.CharField(choices=[('Thin and Crispy', 100), ('Deep Pan', 100), ('Stuffed Crust', 250)], default='Deep Pan', max_length=30),
        ),
    ]
