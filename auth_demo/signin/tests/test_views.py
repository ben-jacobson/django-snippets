from django.test import TestCase
from django.urls import reverse
from .base import create_test_user_and_login, create_test_superhero

class ViewTests(TestCase):
    def test_home_page_renders_template(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_superhero_listView_renders_template(self):
        create_test_user_and_login(client=self.client)
        response = self.client.get(reverse('superhero_listview'))
        self.assertEqual(response.status_code, 200)        
        self.assertTemplateUsed(response, 'superhero_listview.html')

    def test_superhero_detailView_renders_template(self):
        hero_one = create_test_superhero(name='Batman')
        create_test_user_and_login(client=self.client)
        superhero_id = 1
        response = self.client.get(reverse('superhero_detailview', kwargs={'pk': superhero_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'superhero_detailview.html')

    def test_home_page_uses_login_form(self):
        response = self.client.get(reverse('home_page'))
        self.assertContains(response, '<form')

    def test_superhero_listView_contains_test_data(self):
        hero_one = create_test_superhero(name='Batman')
        hero_two = create_test_superhero(name='Iron Man')
        hero_three = create_test_superhero(name='Spiderman')

        create_test_user_and_login(client=self.client)
        response = self.client.get(reverse('superhero_listview'))
        self.assertContains(response, hero_one.name)
        self.assertContains(response, hero_two.name)
        self.assertContains(response, hero_three.name)

    def test_superhero_detailView_contains_test_data(self):
        hero = create_test_superhero(name='Batman')
        create_test_user_and_login(client=self.client)
        response = self.client.get(reverse('superhero_detailview', kwargs={'pk': hero.id}))
        self.assertContains(response, hero.name)
   