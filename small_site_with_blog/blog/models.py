from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=30, help_text="Author Name")  
    email = models.EmailField(unique=True, help_text="Email Address")
    bio = models.TextField(help_text="Author Bio")
    headshot_url = models.URLField(help_text="URL to headshot image")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class Entry(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date_published = models.DateTimeField(null=True, blank=True, help_text="Date Published")
    date_created = models.DateTimeField(default=timezone.localtime, help_text="Date Created") # do we need 'auto_now_add=True'?
    # ManyToOne relationship, one entry can only have one author, however one author can have many entries
    author = models.ForeignKey(Author, on_delete=models.CASCADE)        # When the referenced object is deleted, also delete the objects that have references to it (When you remove a blog post for instance, you might want to delete comments as well).
    title = models.CharField(max_length=255, help_text="Blog Title", default="My Blog Post")  
    html_content = models.TextField(help_text="Blog HTML Content", default="My Blog Content")

    def __str__(self):
        return self.title

    def publish(self, *args, **kwargs):
        self.date_published = timezone.localtime()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-date_published',)     # we want to see most recent published entries on top
        verbose_name_plural = "Entries"

 
