from django.test import TestCase
from signup.forms import CustomerForm

from signup.test_form_data import TEST_FORM_DATA

class FormTests(TestCase):
    def test_form_validation(self):
        # first attempt is to ensure form doesn't validate when it shouldn't
        invalid_form_test_data = {'first_name': 'Test'}
        first_test_form = CustomerForm(data=invalid_form_test_data)
        first_test_form.full_clean()
        self.assertFalse(first_test_form.is_valid(), msg='form.is_valid() should return false since we skipped mandatory fields')

        # second attempt is to ensure form validates when it should
        second_test_form = CustomerForm(data=TEST_FORM_DATA)
        second_test_form.full_clean()
        self.assertTrue(second_test_form.is_valid(), msg='form.is_valid() should return true since weve provided valid data')