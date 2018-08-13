from django.test import TestCase
from .base import create_test_author, create_test_blog_entry

from django.urls import reverse

from datetime import timedelta
from django.utils import timezone


class BlogViewTests(TestCase):
    def setUp(self):
        test_author = create_test_author()
        self.entry_one = create_test_blog_entry(author=test_author)
        self.entry_one.publish()            # publish the first one normally
        self.entry_two = create_test_blog_entry(author=test_author)
        self.entry_two.date_published = timezone.now() + timedelta(days=1)  # publish the second one in tomorrow date
        self.entry_two.save()
        self.entry_three = create_test_blog_entry(author=test_author) # no publish               

    def test_home_uses_correct_template(self):
        response = self.client.get(reverse('home_page'))
        self.assertTemplateUsed(response, 'home.html')

    def test_blog_posts_list_uses_correct_template(self):
        response = self.client.get(reverse('blog_entries'))
        self.assertTemplateUsed(response, 'blog_entries.html')

    def test_blog_post_uses_correct_template(self):
        response = self.client.get(reverse('blog_post', kwargs={'pk': self.entry_one.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_post.html')

    def test_blog_post_response_404_if_published_later_date(self):
        response = self.client.get(reverse('blog_post', kwargs={'pk': self.entry_two.id}))        
        self.assertEqual(response.status_code, 404)

    def test_blog_post_response_404_if_not_published(self):     
        response = self.client.get(reverse('blog_post', kwargs={'pk': self.entry_three.id}))        
        self.assertEqual(response.status_code, 404)

    def test_blog_post_reqponse_404_if_doesnt_exist(self):        
        response = self.client.get(reverse('blog_post', kwargs={'pk': '100'}))        
        self.assertEqual(response.status_code, 404)        