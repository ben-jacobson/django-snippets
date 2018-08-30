from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user
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
        #self.asserFalse(user_.is_authenticated) 
        self.assertEqual(response.status_code, 200, msg='If form is invalid, it shouldnt redirect')
        self.assertContains(response, 'login-error') # Page should have atleast one invalid form message on page

    def test_post_valid_login_data_and_logout(self):
        username = 'test@mctestersonandco.com.au'
        password = 'test1234'
        user_ = create_test_user(username=username, password=password)
        response = self.client.post(reverse('home_page'), {'username': username, 'password': password}) # do we need to use double stars?
        user_ = get_user(self.client)
        self.assertTrue(user_.is_authenticated, msg='Posting login details to home page should authenticate user')

        # page will now redirect to superhero listview
        self.assertRedirects(response, expected_url=reverse('superhero_listview')) # redirection happens too early for this test to pass. Instead we'll just make sure we're on the right page based on it's template

        try:
            self.client.logout()
        except: 
            self.fail('Could not log out, unsure why')
        finally:
            user_ = get_user(self.client)  # need to read the state of the object once more cause caching
            self.assertFalse(user_.is_authenticated, msg='User should now be logged out')

    def test_form_sets_required_fields_as(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200, msg='Home page should load correctly')
        self.assertContains(response, 'required') # Page should have atleast one invalid form message on page