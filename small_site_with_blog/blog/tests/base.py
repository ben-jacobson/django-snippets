from blog.models import Author, Entry
from django.utils import timezone


def create_test_author(name="Authy McAuthface", email="authy@mcauthface.com"):
    test_author = Author(
        name = name, 
        email = email, 
        bio = "I write cool blogs", 
        headshot_url = "http://getdrawings.com/img/female-headshot-silhouette-21.jpg"
    ) 
    test_author.save()
    return test_author
    
def create_test_blog_entry(author, title="default title"):
    test_post = Entry(
        date_created = timezone.now(),
        author = author,
        title = title,
        html_content = "Don't read this..",
    )
    test_post.save()
    return test_post