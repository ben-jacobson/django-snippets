from django.test import TestCase
#from signin.forms import LoginForm
from django.urls import reverse

#from .base import create_test_user

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
        self.assertContains(response, 'Please enter a correct username and password') # Page should have atleast one invalid form message on page

    def test_form_validation(self): 
        self.fail('Finish the test - figure out a way to import the auth form into this test')
        #invalid_form_test_data = {'email_username': 'Invalid Test'}
        #login_test_form = LoginForm(data=invalid_form_test_data)
        #login_test_form.full_clean()
        #self.assertFalse(login_test_form.is_valid(), msg='form.is_valid() should return false since we supplied an invalid username')

        # you can check the various errors produced by the form with form.errors
        #self.assertEqual(login_test_form.errors, {
            #'email_username': ['This field is required.'], # have already supplied a username
        #    'password': ['This field is required.'],           
        #})

    def test_form_sets_fields_as_required(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200, msg='Home page should load correctly')
        self.assertContains(response, 'required') # Page should have atleast one invalid form message on page
