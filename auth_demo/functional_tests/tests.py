from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from signin.tests.base import create_test_user, create_test_superhero

MAX_WAIT = 10 # 10 second max wait

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(MAX_WAIT)
        self.browser.set_page_load_timeout(MAX_WAIT)         

        # the page title is referenced multiple times in tests below, setting a variable in case this changes in future
        self.home_page_title = 'Login to Superhero Database'

        # create some test data for the functional tests
        create_test_superhero(name='Batman')
        create_test_superhero(name='Iron Man')
        create_test_superhero(name='Spiderman')

        # create a set of credentials for testing purposes
        self.test_username = 'test@mctestersonandco.com'
        self.test_password = 'asdf1234'

        # create a test user for all functional tests 
        create_test_user(username=self.test_username, password=self.test_password)

        # assign permissions for all functional tests

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def visit_test_page_and_signin(self, username=None, password=None):
        if username is None:
            username = self.test_username
        if password is None:
            password = self.test_password

        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_username').send_keys(username)
        self.browser.find_element_by_id('id_password').send_keys(password)
        self.browser.find_element_by_id('login-button').click()

    def visit_test_page_and_enter_incorrect_login(self, username='wrong@user.com', password='wrong password'):
        self.visit_test_page_and_signin(username, password)   # just a simple wrapper to aid in code readability

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

class ViewTests(FunctionalTest):
    def test_ListView_has_links_to_DetailView(self):
        self.visit_test_page_and_signin()
        superheroes = self.browser.find_elements_by_class_name('superhero-name')

        # since find_elements returns a list of element objects, we'll need to extract their text before testing
        links_to_superheroes = []
        for element in superheroes:     # produces list of hyperlinks to the superheroes in the database   
            links_to_superheroes.append(element.find_element_by_tag_name('a').get_attribute('href'))

        url_prefix = self.live_server_url + '/superheroes/'
        self.assertEqual(links_to_superheroes, [
            url_prefix + 'batman/',
            url_prefix + 'iron_man/',            
            url_prefix + 'spiderman/',            
        ])

class AuthenticationTests(FunctionalTest):
    def test_user_cannot_access_test_data_without_login(self):
        # user goes directly to page with secret information
        self.browser.get(self.live_server_url + '/superheroes')

        # but notices that they are not able to see this without login, after a few seconds they are redirected to a login page
        self.assertEqual(self.browser.title, self.home_page_title, msg='Accessing the page without logging in should have redirected to home page. May need to tweak wait times before this assert')

    def test_user_can_login_and_see_test_data(self):
        # user visits home page and attempts to log in
        self.visit_test_page_and_signin()
        superheroes = self.browser.find_elements_by_class_name('superhero-name')

        # since find_elements returns a list of element objects, we'll need to extract their text before testing
        text_from_superheroes = []
        for element in superheroes:        # creates ['Batman', 'Iron Man', 'Spiderman']
            text_from_superheroes.append(element.text)

        self.assertIn('Batman', text_from_superheroes)
        self.assertIn('Iron Man', text_from_superheroes)
        self.assertIn('Spiderman', text_from_superheroes)

    def test_user_given_readonly_cannot_edit_data(self):
        # user visits home page and attempts to log in
        self.visit_test_page_and_signin()

        # user sees data and attempts to edit it

        # user is told that they do not have the correct permissions to do this
        self.fail('finish the test')        

    def test_user_given_edit_perm_can_edit_data(self):
        # user visits home page and attempts to log in
        self.visit_test_page_and_signin()

        # user knows that they have correct permissions to edit data

        # user attempts to edit data and succeeeds
        self.fail('finish the test')

class FormValidationTests(FunctionalTest):
    def test_failed_login_attempt_generates_new_csrf(self):
        # finding that if you don't correctly implement the login view, the form's CSRF doens't update.
        # turns out this was user error, I was originally using generic FormView and was able to fix this issue once we switched to generic LoginView
        self.browser.get(self.live_server_url) # unfortunately can't use the visit_test_page_and_enter_incorrect_login since it won't give us the chance to capture the csrf token
        csrf_token = self.browser.find_element_by_name('csrfmiddlewaretoken').get_attribute('value')
        self.browser.find_element_by_id('id_username').send_keys(self.test_username)
        self.browser.find_element_by_id('id_password').send_keys('deliberately entering the wrong password')
        self.browser.find_element_by_id('login-button').click()        
        new_csrf_token = self.browser.find_element_by_name('csrfmiddlewaretoken').get_attribute('value')
        self.assertNotEqual(csrf_token, new_csrf_token)

    def test_form_validation(self):
        self.visit_test_page_and_enter_incorrect_login()
        login_errors = self.browser.find_elements_by_css_selector('.login-error')       # using a css selector cause the error messages may appear as list items, or p tags
        self.assertGreater(len(login_errors), 0, msg='there should be at least one error message on page')
        self.fail('finish this test - need to verify specific errors')