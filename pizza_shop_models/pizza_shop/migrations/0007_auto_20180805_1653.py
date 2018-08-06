# Generated by Django 2.1 on 2018-08-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_shop', '0006_auto_20180805_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='base_cost_cents',
            field=models.IntegerField(default=100, help_text='Pizza base cost in cents'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='base_type',
            field=models.CharField(choices=[('THIN', 'Thin and Crispy'), ('DEEP', 'Deep Pan'), ('STUFFED', 'Stuffed Crust')], default='DEEP', help_text='Type of pizza base to use', max_length=30),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='base_weight_grams',
            field=models.IntegerField(default=200, help_text='Pizza base weight in grams'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='labour_cost_to_make_cents',
            field=models.IntegerField(help_text='Cost of labour in cents'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='margin_percent',
            field=models.IntegerField(help_text='Margin Percentage'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name_on_menu',
            field=models.CharField(help_text='Name', max_length=75, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(help_text='Toppings on this pizza', to='pizza_shop.Topping'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='colour',
            field=models.CharField(choices=[('BL', 'Black'), ('GY', 'Grey'), ('WH', 'White'), ('YE', 'Yellow'), ('BR', 'Brown'), ('PU', 'Purple'), ('GR', 'Green'), ('RE', 'Red'), ('BE', 'Blue')], help_text='Colour', max_length=2),
        ),
        migrations.AlterField(
            model_name='topping',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='ingredient_name',
            field=models.CharField(help_text='Ingredient', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='topping',
            name='portion_cost_cents',
            field=models.IntegerField(help_text='Portion cost in cents'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='portion_weight_grams',
            field=models.IntegerField(help_text='Portion weight in grams'),
        ),
    ]