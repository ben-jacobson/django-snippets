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
            self.toppings[ingredient_name].save()

    def create_test_pizza(self, name_on_menu, labour_cost_to_make_cents, margin_percent, base_type = "DEEP"):
        pizza_ = Pizza(
            name_on_menu =          name_on_menu, 
            labour_cost_to_make_cents =   labour_cost_to_make_cents,
            margin_percent =        margin_percent,
            base_type =             base_type,
        )
        pizza_.save()        
        return pizza_

    def test_pizza_manytomany_relationship_with_toppings(self):
        # create some toppings
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

        self.create_test_topping(
            ingredient_name = "Mushroom", 
            colour = "Gray", 
            portion_weight_grams = 50, 
            portion_cost_cents = 80
        )  

        # create two pizzas

        pizza_one = self.create_test_pizza(
            name_on_menu = "Pepperoni Lovers", 
            labour_cost_to_make_cents = 100, 
            margin_percent = 0.15, 
        )

        pizza_two = self.create_test_pizza(
            name_on_menu = "Pepperoni and Mushrooms", 
            labour_cost_to_make_cents = 100, 
            margin_percent = 0.15, 
        )

        # assign both toppings to pizza_one
        pizza_one.toppings.add(self.toppings["Pepperoni"])
        pizza_one.toppings.add(self.toppings["Cheese"])

        # assign both toppings to pizza_two
        pizza_two.toppings.add(self.toppings["Pepperoni"])
        pizza_two.toppings.add(self.toppings["Cheese"])
        pizza_two.toppings.add(self.toppings["Mushroom"])

        # do the toppings appear on pizza_one?
        self.assertIn(self.toppings["Pepperoni"], Pizza.objects.get(name_on_menu="Pepperoni Lovers").toppings.all())
        self.assertIn(self.toppings["Cheese"], Pizza.objects.get(name_on_menu="Pepperoni Lovers").toppings.all())        

        # do the toppings appear on pizza_two?
        self.assertIn(self.toppings["Pepperoni"], Pizza.objects.get(name_on_menu="Pepperoni and Mushrooms").toppings.all())
        self.assertIn(self.toppings["Cheese"], Pizza.objects.get(name_on_menu="Pepperoni and Mushrooms").toppings.all())            
        self.assertIn(self.toppings["Mushroom"], Pizza.objects.get(name_on_menu="Pepperoni and Mushrooms").toppings.all())            

    def test_pizza_price(self):
        # create toppings and a pizza

        self.create_test_topping(
            ingredient_name = "Pizza Sauce", 
            colour = "Red", 
            portion_weight_grams = 100, 
            portion_cost_cents = 60
        )

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

        test_pizza = self.create_test_pizza(
            name_on_menu = "Pepperoni Lovers", 
            labour_cost_to_make_cents = 100, 
            margin_percent = 1.50, 
            base_type = "STUFFED"
        )

        # add ingredients
        test_pizza.toppings.add(self.toppings["Pizza Sauce"])         
        test_pizza.toppings.add(self.toppings["Pepperoni"])
        test_pizza.toppings.add(self.toppings["Cheese"])

        # calculate the costs of this particular pizza
        calculated_cost = test_pizza.labour_cost_to_make_cents
        calculated_cost += test_pizza.base_cost_cents

        calculated_cost += self.toppings["Pizza Sauce"].portion_cost_cents
        calculated_cost += self.toppings["Pepperoni"].portion_cost_cents
        calculated_cost += self.toppings["Cheese"].portion_cost_cents

        calculated_cost = calculated_cost * (test_pizza.margin_percent + 1)

        self.assertEqual(test_pizza.get_price(), calculated_cost)

    def test_pizza_weight(self):
        # create toppings and a pizza
        self.create_test_topping(
            ingredient_name = "Pizza Sauce", 
            colour = "Red", 
            portion_weight_grams = 100, 
            portion_cost_cents = 60
        )

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

        test_pizza = self.create_test_pizza(
            name_on_menu = "Pepperoni Lovers", 
            labour_cost_to_make_cents = 100, 
            margin_percent = 1.50, 
            base_type = "STUFFED"
        )

        # add ingredients
        test_pizza.toppings.add(self.toppings["Pizza Sauce"])         
        test_pizza.toppings.add(self.toppings["Pepperoni"])
        test_pizza.toppings.add(self.toppings["Cheese"])

        # Calculate the test weight
        calculated_weight = test_pizza.base_weight_grams
        calculated_weight += self.toppings["Pizza Sauce"].portion_weight_grams
        calculated_weight += self.toppings["Pepperoni"].portion_weight_grams
        calculated_weight += self.toppings["Cheese"].portion_weight_grams        

        self.assertEqual(test_pizza.get_weight(), calculated_weight)


''' Basic structure of .add in manytomany relationships

from pizza_shop.models import Pizza, Topping

t1 = Topping(ingredient_name='Cheese', portion_weight_grams=100, portion_cost_cents=50)
t1.save()
t2 = Topping(ingredient_name='Pepperoni', portion_weight_grams=100, portion_cost_cents=50)
t2.save()

p = Pizza(name_on_menu='Pepperoni Lovers', margin_percent=5, labour_cost_to_make_cents=5)
p.save()
p.toppings.add(t1)
p.toppings.add(t2)
p.toppings.all()
'''