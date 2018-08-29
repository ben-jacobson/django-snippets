from django.test import TestCase
from django.urls import reverse
from .base import create_test_user_and_login

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
        create_test_user_and_login(client=self.client)
        superhero_id = 1
        response = self.client.get(reverse('superhero_detailview', kwargs={'pk': superhero_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'superhero_detailview.html')

    def test_home_page_uses_login_form(self):
        response = self.client.get(reverse('home_page'))
        self.assertContains(response, '<form')
        