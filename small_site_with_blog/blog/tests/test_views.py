from django.test import TestCase

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