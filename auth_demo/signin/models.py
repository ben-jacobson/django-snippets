from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Superhero(models.Model):
    name = models.CharField(max_length=100, help_text="Hero Name", unique=True)  
    bio = models.TextField(help_text="Hero Bio")
    picture = models.URLField(help_text="URL to headshot image")
    slug = models.SlugField(unique=True, max_length=120)    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('superhero_detailview', args=[self.slug])

    def create_slug(self, string_to_slug): #slugify is fine, but I prefer underscores
        new_slug = slugify(string_to_slug)
        new_slug = new_slug.replace('-', '_')
        return new_slug

    def save(self, *args, **kwargs):
        self.slug = self.create_slug(self.name)
        super(Superhero, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
