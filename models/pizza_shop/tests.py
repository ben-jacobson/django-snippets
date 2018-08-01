from django.test import TestCase
from .models import Pizza

class PizzaModelTests(TestCase):
    def create_test_toppings(self):
        pass

    def create_test_pizza(self):
        pass

    def test_pizza_manytomany_relationship_with_toppings(self):
        # create two pizzas and two toppings

        # assign both toppings to pizza_one

        # assign both toppings to pizza_two

        # assert that toppings appear on pizza_one

        # assert that toppings appear on pizza_two
        pass

    def test_pizza_price(self):
        # create toppings and a pizza
        # test that the price has been calculated correctly
        pass

    def test_pizza_weight(self):
        # create toppings and a pizza
        # test that the weight of the pizza has been calculated correctly
        pass
