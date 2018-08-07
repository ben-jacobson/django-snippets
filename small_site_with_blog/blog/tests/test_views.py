from django.test import TestCase
#from blog.views import home_page, list_of_blog_posts, blog_entry
from test_models import create_test_author, create_test_blog_entry


class BlogViewTests(TestCase):
    def setUp():
        # All tests require that we have two test blog posts available.
    
    # no need to alter tearDown function yet, default one is fine for now.         

    def test_home_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_list_of_blog_posts_uses_correct_template(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog_entries.html')

    def test_blog_entry_uses_correct_template(self):
        response = self.client.get('/blog/1/')
        self.assertTemplateUsed(response, 'blog_post.html')

    def test_blog_post_list_only_shows_published_entries(self):
        response = self.client.get('/blog/')

        self.fail("unfinished test")
        # next in line to be completed

        # to do after test completion, move create_test_author, create_test_blog_entry into a base.py file
        # also move the setUp function to this, so that for all test_views and test_models have the necessary test entries created


    def test_blog_post_publish_view_redirects(self):
        self.fail("unfinished test")

    def test_blog_post_publish_shows_in_list(self):
        self.fail("unfinished test") 

    def test_post_public_redirects(self):
        self.fail("unfinished test")


