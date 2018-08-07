from django.test import TestCase
from .test_models import create_test_author, create_test_blog_entry

class BlogViewTests(TestCase):
    def setUp(self):
        # All tests require that we have two test blog posts available.
        test_author = create_test_author()

        # establish some test post titles
        self.test_post_title_one = "test post one"
        self.test_post_title_two = "test post two"
        self.test_post_title_unpublished = "we won't publish this one"

        # create some test posts for upcoming tests
        create_test_blog_entry(title=self.test_post_title_one, author=test_author).publish()
        create_test_blog_entry(title=self.test_post_title_two, author=test_author).publish()
        create_test_blog_entry(title=self.test_post_title_unpublished, author=test_author)
    
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
        self.assertContains(response, self.test_post_title_one)
        self.assertContains(response, self.test_post_title_two)   
        self.assertNotContains(response, self.test_post_title_unpublished)
        
    def test_blog_post_publish_view_redirects(self):
        self.fail("unfinished test")

    def test_blog_post_publish_shows_in_list(self):
        self.fail("unfinished test") 

    def test_post_public_redirects(self):
        self.fail("unfinished test")


