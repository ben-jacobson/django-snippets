from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

MAX_WAIT = 10 # 10 second max wait

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(MAX_WAIT)
        self.browser.set_page_load_timeout(MAX_WAIT)
        self.base_url = 'http://localhost:8000' 
        
    def tearDown(self):
        self.browser.quit()
        super().tearDown()

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        '''# User goes to the site
        self.browser.get(self.base_url)
        self.browser.set_window_size(1024, 768)
        
        blog_link = self.browser.find_element_by_link_text('Blog')

        self.assertAlmostEqual(
            blog_link.location['x'] + (blog_link.size['width'] / 2),
            512,
            delta=10
        )'''
        self.fail("functional test to be complete")
   
class ViewBlogPostTest(FunctionalTest):  
    def test_visit_blog_from_home_page(self):
        # User goes to home page, and clicks blog post
        self.browser.get(self.base_url)
        self.browser.find_element_by_link_text('Blog').click()

        blog_entries = self.browser.find_elements_by_css_selector('#blog_entries li')
        self.assertIn("Spam", [row.text for row in blog_entries])
        self.assertIn("Clickbait", [row.text for row in blog_entries])


    def test_post_is_accessible_directly_from_url(self):
        # User is sent a link url and goes directly to it, a page appears

        self.fail("functional test to be complete")

    def test_blog_post_list_only_shows_published_entries(self):
        self.fail("functional test to be complete")                 

class BlogPostingTest(FunctionalTest):
    def test_can_post_blog(self):
        # Site owner goes to the admin page and logs in

        # Site owner clicks blog entries

        # Site owner clicks on create new blog post

        # Site owner drafts a new blog post and saves it

        # Site owner sees that the date created field is correct

        # Site owner notices that the date published field is blank

        # Site owner clicks publish and notices that the date published field is correct
        self.fail("functional test to be complete")        
