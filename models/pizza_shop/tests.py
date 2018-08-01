from django.test import TestCase
from .models import Pizza, Topping

class PizzaModelTests(TestCase):

    def setUp(self):
        self.toppings = {}      # use a dictionary so that the syntax self.toppings["cheese"] can be used

    def create_test_topping(self, ingredient_name, colour, portion_weight_grams, portion_cost_cents):  # create a test toppings and append to the dictionary
        #if not self.toppings[ingredient_name]:             # only create if it doesn't exist already
        if not ingredient_name in self.toppings.keys():             # only create if it doesn't exist already
            self.toppings[ingredient_name] = Topping(
                ingredient_name =       ingredient_name, 
                colour =                colour, 
                portion_weight_grams =  portion_weight_grams, 
                portion_cost_cents =    portion_cost_cents,
            )

    def create_test_pizza(self, name_on_menu, labour_cost_to_make, margin_percent):
        pizza_ = Pizza(
            name_on_menu =          name_on_menu, 
            labour_cost_to_make =   labour_cost_to_make,
            margin_percent =        margin_percent,
        )        
        return pizza_

    def test_pizza_manytomany_relationship_with_toppings(self):
        # create two toppings
        self.create_test_topping(
            ingredient_name = "Pepperoni", 
            colour = "Red", 
            portion_weight_grams = 100, 
            portion_cost_cents = 40
        )

        self.create_test_topping(
            ingredient_name = "Cheese", 
            colour = "Yellow", 
            portion_weight_grams = 120, 
            portion_cost_cents = 160
        )        

        # assign both toppings to pizza_one
        pizza_one = self.create_test_pizza(
            name_on_menu = "Pepperoni Lovers", 
            labour_cost_to_make = 100, 
            margin_percent = 0.15, 
        )

        # add the toppings
        pep = self.toppings["Pepperoni"]
        pizza_one.toppings.create()
        #pizza_one.toppings.add(self.toppings["Cheese"])

        # assign both toppings to pizza_two
        #pizza_two = self.create_test_pizza("Pepperoni with mushrooms", 100, margin_percent, pizza_toppings)

        # do the toppings appear on pizza_one?

        # do the toppings appear on pizza_two?
        pass

    def test_pizza_price(self):
        # create toppings and a pizza
        # test that the price has been calculated correctly
        pass

    def test_pizza_weight(self):
        # create toppings and a pizza
        # test that the weight of the pizza has been calculated correctly
        pass
