from django.test import TestCase
from blog.models import Entry, Author

from datetime import datetime, timedelta

class BlogModelTests(TestCase):
    def create_test_author(self, name="Authy McAuthface", email="authy@mcauthface.com"):
        test_author = Author(
            name = name, 
            email = email, 
            bio = "I write cool blogs", 
            headshot_url = "http://getdrawings.com/img/female-headshot-silhouette-21.jpg"
        ) 
        test_author.save()
        return test_author
        
    def create_test_blog_entry(self, author, title="default title"):
        test_post = Entry(
            date_created = datetime.now(),
            author = author,
            title = "You won't believe how clickbaity this title is",
            html_content = "Don't read this..",
        )
        test_post.save()
        # do not run the save method, since we want to manually publish later. 
        return test_post

    def test_blog_publish_function(self):
        # create the author
        author_ = self.create_test_author()

        # calling the save method of Entry will time stamp the date as now. We need something to compare this to

        # create_test_blog post automatically calls the save function, which acts as a test to ensure null values are allowed in date_published
        entry_ = self.create_test_blog_entry(author=author_)

        # check that it hasn't been published yet until we ask it to
        self.assertIsNone(entry_.date_published)

        # test that the publish function works
        now = datetime.now()
        entry_.publish() 
        self.assertAlmostEqual(now, entry_.date_published, delta=timedelta(seconds=1))         # datetime.timedelta is really useful for this, you can even compare them down to the milliseconds and microseconds. change seconds= to microseconds= and see the difference between the two times.

    def test_blog_onetomany_relationship_with_author(self):
        # create an author
        author_ = self.create_test_author()

        # create two blog posts and assign the authors
        entry_one = self.create_test_blog_entry(author = author_)
        entry_one.save()
        entry_two = self.create_test_blog_entry(author = author_, title="second test blog")
        entry_two.save()

        # does the author appear in the list of authors?
        entries_by_author = Entry.objects.all()
        self.assertEqual(len(entries_by_author), 2)
        self.assertEqual(entries_by_author[0].author, author_)
        self.assertEqual(entries_by_author[1].author, author_)