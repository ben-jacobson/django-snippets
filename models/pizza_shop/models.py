from django.db import models

class Topping(models.Model):
    ingredient_name = models.CharField(max_length=50)

    COLOUR_CHOICES = (
        ('BL', 'Black'),    # i.e olives
        ('GY', 'Grey'),     # i.e Mushrooms                        
        ('WH', 'White'),    # i.e sauces
        ('YE', 'Yellow'),   # Pineapple is a perfectly valid pizza topping, don't let anyone tell you otherwise!
        ('BR', 'Brown'),    # Ground beef
        ('PU', 'Purple'),   # Spanish onions
        ('GR', 'Green'),    # Capsicum, spinach   
        ('RE', 'Red'),      # Capsicum, Sauce, Pepperoni 
        ('BE', 'Blue'),     # What kind of topping would be blue?!                
    )
    colour = models.CharField(max_length=2, choices=COLOUR_CHOICES)

    # when applying a topping to a pizza, you grab a handful and ideally it should weight this much, and therefore cost can be determined too
    portion_weight_grams = models.IntegerField()
    portion_cost_cents = models.IntegerField()    

    def __str__(self):
        return self.ingredient_name    

    class Meta:
        ordering = ('ingredient_name',)        

class Pizza(models.Model):
    name_on_menu = models.CharField(max_length=75, primary_key=True)
    labour_cost_to_make = models.IntegerField()
    margin_percent = models.IntegerField()
    toppings = models.ManyToManyField(Topping)

    def get_price(self):
        pass

    def get_weight(self):
        pass

    def __str__(self):
        return self.name_on_menu

    class Meta:
        ordering = ('name_on_menu',)



# Chasing a bug all day, time to push this into the code

'''
from pizza_shop.models import Pizza, Topping
from django.db.utils import IntegrityError

t1 = Topping(ingredient_name='Cheese', portion_weight_grams=100, portion_cost_cents=50)
t1.save()
t2 = Topping(ingredient_name='Pepperoni', portion_weight_grams=100, portion_cost_cents=50)
t2.save()

p = Pizza(name_on_menu='Pepperoni Lovers', margin_percent=5, labour_cost_to_make=5)
p.save()
p.toppings.add(t1)
p.toppings.add(t2)
p.toppings.all()

'''