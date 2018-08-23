from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

from signup.models import Customer

MAX_WAIT = 10 # 10 second max wait

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(MAX_WAIT)
        self.browser.set_page_load_timeout(MAX_WAIT)

        # some test data to include into the form and test against.
        self.first_name = "Tester"
        self.middle_name = "Selenium"
        self.surname = "McTesterson"

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def input_test_data_into_customer_form(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("id_title").send_keys("m")  # should default to Mr
        self.browser.find_element_by_id("id_first_name").send_keys(self.first_name)
        self.browser.find_element_by_id("id_middle_name").send_keys(self.middle_name)
        self.browser.find_element_by_id("id_surname").send_keys(self.surname)
        self.browser.find_element_by_id("id_gender").send_keys("Male")
        self.browser.find_element_by_id("id_dob").send_keys("2018-08-31")
        self.browser.find_element_by_id("id_email").send_keys("tester@mctestersonandco.com")
        self.browser.find_element_by_id("id_phone").send_keys("6665468")
        self.browser.find_element_by_id("id_mobile").send_keys("7771243")
        self.browser.find_element_by_id("id_address_1").send_keys("Unit Test")
        self.browser.find_element_by_id("id_address_2").send_keys("123 Test St")
        self.browser.find_element_by_id("id_city").send_keys("Testville")
        self.browser.find_element_by_id("id_state").send_keys("Test State")
        self.browser.find_element_by_id("id_country").send_keys("au") # will default to Australia

class FormTest(FunctionalTest):
    def test_input_customer_data(self):
        # data is entered into the form
        self.input_test_data_into_customer_form()

        # the user then clicks the submit button
        self.browser.find_element_by_id("submit").click()
     
        # check to see that the data is now in the database. TODO - figure out how to make this a model test somehow
        cust_data = Customer.objects.get(id=1)
        self.assertEqual(cust_data.first_name, self.first_name)
        self.assertEqual(cust_data.middle_name, self.middle_name)
        self.assertEqual(cust_data.surname, self.surname)

