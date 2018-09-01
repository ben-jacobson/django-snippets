from django.test import TestCase
from .base import create_test_superhero

class ModelTests(TestCase): 
    def test_make_slug_on_create(self):
        hero = create_test_superhero(name='This Is A Hero Name')
        self.assertEquals(hero.name, 'This Is A Hero Name')
        self.assertEquals(hero.slug, 'this_is_a_hero_name')
