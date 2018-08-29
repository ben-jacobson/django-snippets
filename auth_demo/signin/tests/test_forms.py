from django.test import TestCase
#from signin.forms import LoginForm
from django.urls import reverse

from .base import create_test_user

class LoginFormTests(TestCase): 
    def test_post_invalid_username_andor_password(self):
        # deliberately don't create any users 
        #user_ = create_test_user(username='test@test.com.au', password='asdf1234') # If you want to ensure this test can fail, uncomment below

        test_login_data = {
            'email_username': 'test@test.com.au',
            'password': 'asdf1234',
        }        
        response = self.client.post(reverse('home_page'), test_login_data)
        self.assertEqual(response.status_code, 200, msg='If form is invalid, it shouldnt redirect')
        self.assertContains(response, 'login-error') # Page should have atleast one invalid form message on page

    def test_post_valid_login_data_and_logout(self):
        test_login_data = {
            'email_username': 'test@mctestersonandco.com.au',
            'password': 'test1234',
        }
        user_ = create_test_user(username=test_login_data['email_username'], password=test_login_data['password'])
        response = self.client.post(reverse('home_page'), test_login_data)
        #self.assertRedirects(response, expected_url=reverse('superhero_listview'))
        self.assertContains(response, 'Superhero Database') 
        self.assertContains(response, 'Log out')

        try:
            self.client.logout()
        except: 
            self.fail('Could not log out, unsure why')

        user_.delete()    # delinting - unused user_ is throwing unused error 
        self.assertRedirects(response, expected_url=reverse('home_page'))

    def test_form_sets_required_fields_as(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200, msg='Home page should load correctly')
        self.assertContains(response, 'required') # Page should have atleast one invalid form message on page