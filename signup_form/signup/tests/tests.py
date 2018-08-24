from django.test import TestCase
from signup.models import Customer
from signup.test_form_data import TEST_FORM_DATA
from django.urls import reverse

#from signup.forms import CustomerForm

class FormViewTests(TestCase): 
# when using CreateView, you'll only need two tests, one to post the formdata, the other to ensure it's reached the database
    
    def test_post_customer_data(self):
        # simulates posting the form data to the home page, just like the form would, then asserts that it lands in the database
        response = self.client.post(reverse('home_page'), TEST_FORM_DATA)
        self.assertEqual(response.status_code, 302, msg='When posting form data, page does not redirect')
        self.assertEqual(Customer.objects.last().email, TEST_FORM_DATA['email'])
    
    def test_post_customer_validation_check(self):
        copy_of_test_form_data = dict(TEST_FORM_DATA)   # This has tricked me more than once in the past.. Python doesn't create copies of objects unless you explicitly tell it to. Alternative is dict.copy()
        copy_of_test_form_data['dob'] = 'Invalid'
        response = self.client.post(reverse('home_page'), copy_of_test_form_data)
        self.assertEqual(response.status_code, 200, msg='If form is invalid, it wont redirect')
        self.assertContains(response, 'Enter a valid date.') # Page should have atleast one invalid form message on page

    def test_post_customer_blank_fields(self):
        # this test doesn't actually work for testing the behaviour, simply only tests whether or not one or more fields are marked with the 'required' html form attribute
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200, msg='Home page should load correctly')
        self.assertContains(response, 'required') # Page should have atleast one invalid form message on page

    def test_post_customer_duplicate_data(self):
        response = self.client.post(reverse('home_page'), TEST_FORM_DATA) 
        self.assertEqual(response.status_code, 302, msg='Should redirect since the form is valid')
        response = self.client.post(reverse('home_page'), TEST_FORM_DATA) # attempt to post the same data twice.     
        self.assertEqual(response.status_code, 200, msg='If form is invalid, it wont redirect')
        self.assertContains(response, 'Customer with this Email already exists.') 
        
    def test_customer_data_appears_on_thanks(self):
        cust_data = Customer.objects.create(**TEST_FORM_DATA)    # ** allows us to pass a dictionary through to the create method, so long as the dict entries match the model fields
        response = self.client.get(cust_data.get_success_url())
        self.assertEqual(response.status_code, 200, msg='thanks page should load 200 OK')
        self.assertContains(response, TEST_FORM_DATA['email'])

'''class FormTests(TestCase):  # when using a form view, we were able to call the form directly and test it's validation, since we switched to CreateView, we can no longer do this. commenting out, but good to see how below you can view how to test validation errors, required fields, etc. 
    def test_form_validation(self):
        # first attempt is to ensure form doesn't validate when it shouldn't
        invalid_form_test_data = {'first_name': 'Test'}
        first_test_form = CustomerForm(data=invalid_form_test_data)
        first_test_form.full_clean()
        self.assertFalse(first_test_form.is_valid(), msg='form.is_valid() should return false since we skipped mandatory fields')

        # you can check the various errors produced by the form with form.errors
        self.assertEqual(first_test_form.errors, {
            #'first_name': ['This field is required.'], # have already supplied a first name
            'surname': ['This field is required.'],
            'gender': ['This field is required.'],
            'dob': ['This field is required.'],
            'email': ['This field is required.'],
            'address_1': ['This field is required.'],
            'city': ['This field is required.'],
            'state': ['This field is required.'],
            'country': ['This field is required.'],            
        })

        # second attempt is to ensure form validates when it should
        second_test_form = CustomerForm(data=TEST_FORM_DATA)
        second_test_form.full_clean()
        self.assertTrue(second_test_form.is_valid(), msg='form.is_valid() should return true since weve provided valid data') 
 
    def test_form_saves_data_to_database(self):
        test_form = CustomerForm(data=TEST_FORM_DATA)
        test_form.full_clean()
        form_object_test = test_form.save()     

        # check first that the form object contains the data. Save() creates a new object for us to test
        self.assertEqual(form_object_test.first_name, TEST_FORM_DATA['first_name'])
        self.assertEqual(form_object_test.middle_name, TEST_FORM_DATA['middle_name'])
        self.assertEqual(form_object_test.surname, TEST_FORM_DATA['surname'])         

        # then check that the date can be read from the database
        cust_data = Customer.objects.get(email=TEST_FORM_DATA['email'])
        self.assertEqual(cust_data.first_name, TEST_FORM_DATA['first_name'])
        self.assertEqual(cust_data.middle_name, TEST_FORM_DATA['middle_name'])
        self.assertEqual(cust_data.surname, TEST_FORM_DATA['surname'])

'''