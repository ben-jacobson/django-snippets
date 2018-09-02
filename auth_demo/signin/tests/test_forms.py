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

class SuperheroEditTest(TestCase):
    def test_post_page_edits(self):
        # simulates posting the form data to the home page, just like the form would, then asserts that it lands in the database
        #response = self.client.post(reverse('home_page'), TEST_FORM_DATA)
        #self.assertEqual(response.status_code, 302, msg='When posting form data, page does not redirect')
        #self.assertEqual(Customer.objects.last().email, TEST_FORM_DATA['email'])
        self.fail('Finish the test')

    def test_post_validation_check(self):
        #copy_of_test_form_data = dict(TEST_FORM_DATA)   # This has tricked me more than once in the past.. Python doesn't create copies of objects unle$
        #copy_of_test_form_data['dob'] = 'Invalid'
        #response = self.client.post(reverse('home_page'), copy_of_test_form_data)
        #self.assertEqual(response.status_code, 200, msg='If form is invalid, it wont redirect')
        #self.assertContains(response, 'Enter a valid date.') # Page should have atleast one invalid form message on page
        self.fail('Finish the test')

    def test_post_blank_fields(self):
        # this test doesn't actually work for testing the behaviour, simply only tests whether or not one or more fields are marked with the 'required'$
        #response = self.client.get(reverse('home_page'))
        #self.assertEqual(response.status_code, 200, msg='Home page should load correctly')
        #self.assertContains(response, 'required') # Page should have atleast one invalid form message on page
        self.fail('Finish the test')

    def test_post_duplicate_data(self):
        #response = self.client.post(reverse('home_page'), TEST_FORM_DATA) 
        #self.assertEqual(response.status_code, 302, msg='Should redirect since the form is valid')
        #response = self.client.post(reverse('home_page'), TEST_FORM_DATA) # attempt to post the same data twice.     
        #self.assertEqual(response.status_code, 200, msg='If form is invalid, it wont redirect')
        #self.assertContains(response, 'Customer with this Email already exists.') 
        self.fail('Finish the test')

    def test_post_data_appears_on_modelForm(self):
        #cust_data = Customer.objects.create(**TEST_FORM_DATA)    # ** allows us to pass a dictionary through to the create method, so long as the dict $
        #response = self.client.get(cust_data.get_success_url())
        #self.assertEqual(response.status_code, 200, msg='thanks page should load 200 OK')
        #self.assertContains(response, TEST_FORM_DATA['email'])
        self.fail('Finish the test')