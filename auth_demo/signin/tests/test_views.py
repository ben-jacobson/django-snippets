from django.test import TestCase
from django.urls import reverse

class ViewTests(TestCase):
    def test_home_page_renders_template(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_superhero_listView_renders_template(self):
        self.fail('need to go back and create a logged in user first')
        response = self.client.get(reverse('superhero_listview'))
        self.assertEqual(response.status_code, 200)        
        self.assertTemplateUsed(response, 'superhero_listview.html')

    def test_superhero_detailView_renders_template(self):
        self.fail('need to go back and create a logged in user, and some dummy superhero data')
        superhero_id = 1
        response = self.client.get(reverse('superhero_detailview', kwargs={'pk': superhero_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'superhero_detailview.html')

    def test_home_page_uses_login_form(self):
        #response = self.client.get(reverse('home_page'))
        #self.assertIsInstance(response.context['form'], ItemForm)
        self.fail("Finish this test - ensure we can test the form somehow")        