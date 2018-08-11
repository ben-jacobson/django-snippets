from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date
from django.contrib.auth import get_user_model
from blog.tests.base import create_test_author, create_test_blog_entry

#from time import sleep

MAX_WAIT = 10 # 10 second max wait

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(MAX_WAIT)
        self.browser.set_page_load_timeout(MAX_WAIT)

        # We'll need an author in the test database
        self.test_author_name = 'Test Author'
        self.test_email = 'test@test.com'
        test_author = create_test_author(name=self.test_author_name, email=self.test_email)        
        
        # We'll also need 3 test posts, 2 published, 1 unpublished
        test_post_one = create_test_blog_entry(title="Spam", author=test_author)
        test_post_one.publish()
        test_post_two = create_test_blog_entry(title="Clickbait", author=test_author)
        test_post_two.publish()
        create_test_blog_entry(title="Unpublished", author=test_author)
        # don't publish the last one

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # For now, this snippet won't include any CSS. So we'll simply assert that the correct title is in use. Replace this

        # User goes to the site
        self.browser.get(self.live_server_url)          # LiveServerTestCase will automatically set the correct url + port for it's test server
        self.assertEqual('Simple site with a blog post', self.browser.title)   
   
class ViewBlogPostTest(FunctionalTest):  
    def test_visit_blog_from_home_page(self):
        # User goes to home page, and clicks blog post
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text('Blog').click()

        blog_entries = self.browser.find_elements_by_css_selector('#blog_entries li')
        self.assertIn("Spam", [row.text for row in blog_entries])
        self.assertIn("Clickbait", [row.text for row in blog_entries])
        self.assertNotIn("Unpublished", [row.text for row in blog_entries])

    def test_visit_blog_entry_from_list(self):
        # User visits the blog post list
        self.browser.get(self.live_server_url + '/blog/')

        # selects the first post from the list and clicks it
        blog_link = self.browser.find_element_by_class_name('blog_post')
        blog_title = blog_link.text
        blog_link.click()

        # check that the page title is correct
        self.assertIn(blog_title, self.browser.find_element_by_tag_name('h1').text)
    
    def test_blog_post_shows_error_message_if_not_published(self):
        self.fail("Complete this test")      

class BlogPostingTest(FunctionalTest):
    def test_can_post_blog_using_admin_page(self):
        # Because we are using LiveServerTestCase, it won't have the super user already set, we'll need to set this.
        admin_page_user = 'admin'
        admin_page_pass = 'blogpost'

        User = get_user_model() 
        User.objects.create_superuser(admin_page_user, self.test_email, admin_page_pass)        

        # Site owner goes to the admin page and logs in
        self.browser.get(self.live_server_url + '/admin')
        self.browser.find_element_by_id('id_username').send_keys(admin_page_user)
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys(admin_page_pass)
        password_box.send_keys(Keys.ENTER)

        # Site owner clicks blog entries
        self.browser.find_element_by_link_text('Entries').click()

        # Site owner finds the option to draft a new blog post and clicks it
        self.browser.find_element_by_class_name('addlink').click()

        # Site owner drafts a new blog post and saves it
        # starting with setting date drafted
        todays_date = str(date.today())
        self.browser.find_element_by_id('id_date_created').send_keys(todays_date)

        # then selects the author from the drop down menu
        self.browser.find_element_by_id('id_author').send_keys(self.test_author_name)
        
        # site owner inputs Title and HTML content
        test_title = 'Test Blog Post'
        title_box = self.browser.find_element_by_id('id_title')
        title_box.clear()
        title_box.send_keys(test_title)

        content_box = self.browser.find_element_by_id('id_html_content')
        content_box.clear()
        content_box.send_keys('Content goes here!')

        # and hits save
        self.browser.find_element_by_name('_save').click()

        # site owner goes back to entries and finds the new blog post there waiting for him
        self.assertEqual(test_title, self.browser.find_element_by_link_text(test_title).text)


        