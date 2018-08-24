from django.test import TestCase
from signup.forms import CustomerForm
from signup.models import Customer

from signup.test_form_data import TEST_FORM_DATA

class FormTests(TestCase):
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