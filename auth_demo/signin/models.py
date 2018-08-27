from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=100, help_text="Hero Name", unique=True)  
    bio = models.TextField(help_text="Hero Bio")
    picture = models.URLField(help_text="URL to headshot image")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
