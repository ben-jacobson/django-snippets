from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10 # 10 second max wait

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(MAX_WAIT)
        self.browser.set_page_load_timeout(MAX_WAIT)         

        # the page title is referenced multiple times in tests below, setting a variable in case this changes in future
        self.home_page_title = 'Login to Superhero Database'

        # create a set of credentials for testing purposes
        self.test_username = 'test@mctestersonandco.com'
        self.test_password = 'asdf1234'

        # create a test user for all functional tests 

        # assign permissions for all functional tests

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def visit_test_page_and_signin(self, username, password):
        self.browser.get(self.live_server_url)
        pass

class LayoutAndStylingTest(FunctionalTest):
    def test_signin_page_form(self):
        # user visits home page and sees a signin page
        self.browser.get(self.live_server_url)
        page_title = self.browser.title
        
        #... notices that the page title says 'Login to Superhero Database', same with the page header
        self.assertEqual(page_title, self.home_page_title, msg='Page title should be: "Login to Superhero Database"')
        page_header = self.browser.find_element_by_css_selector('h1.page-title').get_attribute("innerText")
        self.assertEqual(page_header, self.home_page_title, msg='Page header should be same as page title')
        
        #... notices that there is a form on the page, with a button that says 'Login'
        self.assertEqual(self.browser.find_element_by_id('login-button').get_attribute('value'), 'Login', msg='Form submit button should read "Login"')

class AuthenticationTests(FunctionalTest):
    def test_user_cannot_access_test_data_without_login(self):
        # user goes directly to page with secret information
        self.browser.get(self.live_server_url + '/superheroes')

        # but notices that they are not able to see this without login, after a few seconds they are redirected to a login page
        self.assertEqual(self.browser.title, self.home_page_title, msg='Accessing the page without logging in should have redirected to home page. May need to tweak wait times before this assert')

    def test_user_can_login_and_see_test_data(self):
        # user visits home page and attempts to log in
        self.visit_test_page_and_signin(username=self.test_username, password=self.test_password)
        self.fail('finish the test')

    def test_user_given_readonly_cannot_edit_data(self):
        # user visits home page and attempts to log in
        self.visit_test_page_and_signin(username=self.test_username, password=self.test_password)

        # user sees data and attempts to edit it

        # user is told that they do not have the correct permissions to do this
        self.fail('finish the test')        

    def test_user_given_edit_perm_can_edit_data(self):
        # user visits home page and attempts to log in
        self.visit_test_page_and_signin(username=self.test_username, password=self.test_password)

        # user knows that they have correct permissions to edit data

        # user attempts to edit data and succeeeds
        self.fail('finish the test')

class FormValidationTests(FunctionalTest):
    def test_failed_login_attempt_generates_new_csrf(self):
        # finding that if you don't correctly implement the login view, the form's CSRF doens't update.
        # turns out this was user error, I was originally using generic FormView and was able to fix this issue once we switched to generic LoginView
        self.fail('finish the test')

    def test_form_validation(self):
        self.fail('finish the test')