from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Superhero(models.Model):
    name = models.CharField(max_length=100, verbose_name="Hero Name", unique=True)  
    bio = models.TextField(verbose_name="Hero Bio")
    picture = models.URLField(verbose_name="URL to headshot image")
    slug = models.SlugField(unique=True, max_length=120)    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('superhero_detailview', args=[self.slug])

    def get_edit_url(self):
        return reverse('superhero_editview', args=[self.slug])

    def create_slug(self, string_to_slug): #slugify is fine, but I prefer underscores
        new_slug = slugify(string_to_slug)
        new_slug = new_slug.replace('-', '_')
        return new_slug

    def save(self, *args, **kwargs):
        self.slug = self.create_slug(self.name)
        super(Superhero, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
