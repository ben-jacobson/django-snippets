from django.test import TestCase
#from blog.views import home_page, list_of_blog_posts, blog_entry

class BlogViewTests(TestCase):
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
        self.fail("unfinished test")
        pass   

    def test_blog_post_publish_view_redirects(self):
        self.fail("unfinished test")
        pass 

    def test_blog_post_publish_shows_in_list(self):
        self.fail("unfinished test") 
        pass

    def test_post_public_redirects(self):
        self.fail("unfinished test")
        pass 


