from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from blog.tests.test_models import create_test_author, create_test_blog_entry

MAX_WAIT = 10 # 10 second max wait

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(MAX_WAIT)
        self.browser.set_page_load_timeout(MAX_WAIT)

        # set up method is run for each test, for the sake of all tests, we will have 2 blog posts created for functional testing. This code will just create as part of the model
        author = create_test_author()
        create_test_blog_entry(author=author, title="functional test one")
        create_test_blog_entry(author=author, title="functional test two")
        
    def tearDown(self):
        self.browser.quit()
        super().tearDown()

class LayoutAndStylingTest(FunctionalTest):
    def test_home_page_correct_layout(self):
        # User goes to the site
        
        # and notices that the page has a link to a blog

        self.fail("functional test to be complete")

    def test_blog_post_listings_page_has_correct_layout(self):
        # User goes to the site and clicks on the blog link

        # and notices that there are is a header "Blog Posts"

        self.fail("functional test to be complete")

    def test_blog_post_has_correct_layout(self):
        # User goes to the blog post list page

        # And clicks the first blog post in the list called "Test Blog"

        # The user clicks it and finds that the title of the page is "Test Blog"

        self.fail("functional test to be complete")             
   
class ViewBlogPostTest(FunctionalTest):    
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
