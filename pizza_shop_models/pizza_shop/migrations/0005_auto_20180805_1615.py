# Generated by Django 2.1 on 2018-08-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_shop', '0004_pizza_base_weight_grams'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='labour_cost_to_make',
            new_name='labour_cost_to_make_cents',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='base_weight_grams',
            field=models.IntegerField(default=200),
        ),
    ]
