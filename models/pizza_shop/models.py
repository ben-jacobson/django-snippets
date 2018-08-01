from django.db import models

class Topping(models.Model):
    ingredient_name = models.CharField(max_length=50, primary_key = True)

    COLOUR_CHOICES = (
        ('BL', 'Black'),    # i.e olives
        ('GR', 'Grey'),     # i.e Mushrooms                        
        ('WH', 'White'),    # i.e sauces
        ('YE', 'Yellow'),   # Pineapple is a perfectly valid pizza topping, don't let anyone tell you otherwise!
        ('BR', 'Brown'),    # Ground beef
        ('PU', 'Purple'),   # Spanish onions
        ('GR', 'Green'),    # Capsicum, spinach   
        ('RE', 'Red'),      # Capsicum, Sauce, Pepperoni 
        ('BL', 'Blue'),     # What kind of topping would be blue?!                
    )
    colour = models.CharField(max_length=2, choices=COLOUR_CHOICES)

    # when applying a topping to a pizza, you grab a handful and ideally it should weight this much, and therefore cost can be determined too
    portion_weight = models.IntegerField()
    portion_cost = models.IntegerField()

class Pizza(models.Model):
    name_on_menu = models.CharField(max_length=75, primary_key = True)
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
        ordering = ["name_on_menu"]