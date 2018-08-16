from django.test import TestCase
from blog.models import Entry#, Author
from .base import create_test_author, create_test_blog_entry

from django.utils import timezone
from datetime import timedelta

class BlogModelTests(TestCase):
    def test_blog_publish_function(self):
        # create the author
        author_ = create_test_author()

        # calling the save method of Entry will time stamp the date as now. We need something to compare this to

        # create_test_blog post automatically calls the save function, which acts as a test to ensure null values are allowed in date_published
        entry_ = create_test_blog_entry(author=author_)

        # check that it hasn't been published yet until we ask it to
        self.assertIsNone(entry_.date_published)

        # test that the publish function works
        entry_.publish() 
        self.assertAlmostEqual(timezone.localtime(timezone.localtime()), entry_.date_published, delta=timedelta(seconds=1))         # datetime.timedelta is really useful for this, you can even compare them down to the milliseconds and microseconds. change seconds= to microseconds= and see the difference between the two times.

    def test_blog_onetomany_relationship_with_author(self):
        # create an author
        author_ = create_test_author()

        # create two blog posts and assign the authors
        entry_one = create_test_blog_entry(author = author_)
        entry_one.save()
        entry_two = create_test_blog_entry(author = author_, title="second test blog")
        entry_two.save()

        # does the author appear in the list of authors?
        entries_by_author = Entry.objects.all()
        self.assertEqual(len(entries_by_author), 2)
        self.assertEqual(entries_by_author[0].author, author_)
        self.assertEqual(entries_by_author[1].author, author_)

    def test_blog_ordering(self):
        author_ = create_test_author()
        entry_one = create_test_blog_entry(title="post one", author = author_)
        entry_two = create_test_blog_entry(title="post two", author = author_)
        entry_three = create_test_blog_entry(title="post three", author = author_)
        entry_one.publish()
        entry_two.publish()
        entry_three.publish()

        entries = Entry.objects.all().filter(date_published__lte=timezone.localtime())  # only get published entries, since date_pubished is how it is ordered
        self.assertEqual(len(entries), 3)

        # Entries should be ordered the most recent date_published first, through to least recent
        entry_titles_in_correct_order = ['post three', 'post two', 'post one']
        entry_titles_of_test_posts = []

        for e in entries:
            entry_titles_of_test_posts.append(e.title)

        self.assertEqual(entry_titles_in_correct_order, entry_titles_of_test_posts)

