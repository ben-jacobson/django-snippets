from django.contrib import admin
from .models import Author, Entry

admin.site.register(Author)
admin.site.register(Entry, name="Entries")