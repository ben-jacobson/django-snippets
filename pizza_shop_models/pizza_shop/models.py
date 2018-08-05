from django.db import models

class Topping(models.Model):
    ingredient_name = models.CharField(max_length=50, unique=True, help_text="Ingredient")

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
    colour = models.CharField(max_length=2, choices=COLOUR_CHOICES, help_text="Colour")

    # when applying a topping to a pizza, you grab a handful and ideally it should weight this much, and therefore cost can be determined too
    portion_weight_grams = models.IntegerField(help_text="Portion weight in grams")
    portion_cost_cents = models.IntegerField(help_text="Portion cost in cents")    

    def __str__(self):
        return self.ingredient_name    

    class Meta:
        ordering = ('ingredient_name',)        

class Pizza(models.Model):
    name_on_menu = models.CharField(max_length=75, primary_key=True, help_text="Name")
    labour_cost_to_make_cents = models.IntegerField(help_text="Cost of labour in cents")
    margin_percent = models.IntegerField(help_text="Margin Percentage")
    
    BASES = (  ## Base types
        ('THIN', 'Thin and Crispy'),
        ('DEEP', 'Deep Pan'),
        ('STUFFED', 'Stuffed Crust'),
    )
    
    BASE_COSTS = { # costs of bases
        'THIN': 100, 
        'DEEP': 100,
        'STUFFED': 250,
    }    

    BASE_WEIGHTS = {
        'THIN': 150, 
        'DEEP': 200,
        'STUFFED': 300,        
    }

    base_type = models.CharField(max_length=30, choices=BASES, default='DEEP', help_text="Type of pizza base to use")
    base_cost_cents = models.IntegerField(default=BASE_COSTS['DEEP'], help_text="Pizza base cost in cents")    # cost of the pizza_base
    base_weight_grams = models.IntegerField(default=BASE_WEIGHTS['DEEP'], help_text="Pizza base weight in grams")    # cost of the pizza_base

    toppings = models.ManyToManyField(Topping, help_text="Toppings on this pizza")

    def save(self, *args, **kwargs):
        # Overwritten the save method, so that the base_cost_cents is populated automatically, based on the chosen base type
        self.base_cost_cents = self.BASE_COSTS[self.base_type]
        self.base_weight_grams = self.BASE_WEIGHTS[self.base_type]
        super().save(*args, **kwargs)

    def get_price(self):
        # start with the pizza base cost
        calculated_price = self.base_cost_cents       

        # then add cost of toppings
        for topping in self.toppings.all():
            calculated_price += topping.portion_cost_cents

        # then add labour cost
        calculated_price += self.labour_cost_to_make_cents

        # then add margin
        calculated_price = calculated_price * (1 + self.margin_percent)

        return calculated_price

    def get_weight(self):
        # start with the weight of the pizza_base
        calculated_weight = self.base_weight_grams

        # then add weight of toppings
        for topping in self.toppings.all():
            calculated_weight += topping.portion_weight_grams

        return calculated_weight

    def __str__(self):
        return self.name_on_menu

    class Meta:
        ordering = ('name_on_menu',)