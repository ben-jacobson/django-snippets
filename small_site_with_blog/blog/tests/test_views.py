from django.test import TestCase
from blog.views import list_of_blog_posts, blog_entry

class BlogViewTests(TestCase):
    def test_home_uses_correct_template(self):
        #response = self.client.get('/')
        #self.assertTemplateUsed(response, 'home.html')
        self.fail("unfinished test")

    def test_blog_post_list_uses_correct_template(self):
        self.fail("unfinished test")

    def test_blog_entry_uses_correct_template(self):
        self.fail("unfinished test")   

    def test_blog_post_publish_view_redirects(self):
        self.fail("unfinished test") 

    def test_blog_post_publish_shows_in_list(self):
        self.fail("unfinished test") 


