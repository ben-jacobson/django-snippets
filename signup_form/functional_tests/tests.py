from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10 # 10 second max wait

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(MAX_WAIT)
        self.browser.set_page_load_timeout(MAX_WAIT)

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

class LayoutAndStylingTest(FunctionalTest):
    def test_fail(self):
        self.fail("complete these tests")
