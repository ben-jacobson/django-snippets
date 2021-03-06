# Generated by Django 2.1 on 2018-08-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('name_on_menu', models.CharField(max_length=75, primary_key=True, serialize=False)),
                ('labour_cost_to_make', models.IntegerField()),
                ('margin_percent', models.IntegerField()),
            ],
            options={
                'ordering': ('name_on_menu',),
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=50)),
                ('colour', models.CharField(choices=[('BL', 'Black'), ('GY', 'Grey'), ('WH', 'White'), ('YE', 'Yellow'), ('BR', 'Brown'), ('PU', 'Purple'), ('GR', 'Green'), ('RE', 'Red'), ('BE', 'Blue')], max_length=2)),
                ('portion_weight_grams', models.IntegerField()),
                ('portion_cost_cents', models.IntegerField()),
            ],
            options={
                'ordering': ('ingredient_name',),
            },
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='pizza_shop.Topping'),
        ),
    ]
