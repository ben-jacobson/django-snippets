from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

#from signup.models import Customer
from signup.test_form_data import TEST_FORM_DATA

MAX_WAIT = 10 # 10 second max wait

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(MAX_WAIT)
        self.browser.set_page_load_timeout(MAX_WAIT)

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def input_test_data_into_customer_form(self):
        self.browser.find_element_by_id("id_title").send_keys('m')  # should default to Mr
        self.browser.find_element_by_id("id_first_name").send_keys(TEST_FORM_DATA['first_name'])
        self.browser.find_element_by_id("id_middle_name").send_keys(TEST_FORM_DATA['middle_name'])
        self.browser.find_element_by_id("id_surname").send_keys(TEST_FORM_DATA['surname'])
        self.browser.find_element_by_id("id_gender").send_keys(TEST_FORM_DATA['gender'])
        self.browser.find_element_by_id("id_dob").send_keys(TEST_FORM_DATA['dob'])
        self.browser.find_element_by_id("id_email").send_keys(TEST_FORM_DATA['email'])
        self.browser.find_element_by_id("id_phone").send_keys(TEST_FORM_DATA['phone'])
        self.browser.find_element_by_id("id_mobile").send_keys(TEST_FORM_DATA['mobile'])
        self.browser.find_element_by_id("id_address_1").send_keys(TEST_FORM_DATA['address_1'])
        self.browser.find_element_by_id("id_address_2").send_keys(TEST_FORM_DATA['address_2'])
        self.browser.find_element_by_id("id_city").send_keys(TEST_FORM_DATA['city'])
        self.browser.find_element_by_id("id_state").send_keys(TEST_FORM_DATA['state'])
        self.browser.find_element_by_id("id_country").send_keys('Au')

class FormTest(FunctionalTest):
    def test_input_customer_data_creates_database_entries(self):
        # user navigates to form page
        self.browser.get(self.live_server_url)

        # data is entered into the form
        self.input_test_data_into_customer_form()

        # the user then clicks the submit button
        self.browser.find_element_by_id("submit").click()
     
        # check to see that the data is now visible on the page.  
        test_full_name = TEST_FORM_DATA['first_name'] + " " + TEST_FORM_DATA['surname']
        self.assertEqual(test_full_name, self.browser.find_element_by_id('customer-name').get_attribute("innerText"), msg='Name not appearing on /thanks/ page')
        self.assertEqual(TEST_FORM_DATA['email'], self.browser.find_element_by_id('customer-email').get_attribute("innerText"), 'Email not appearing on /thanks/ page')

    def test_input_invalid_data_shows_errors(self):
        self.fail('finish this test')