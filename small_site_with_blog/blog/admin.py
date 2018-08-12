from django.contrib import admin
from .models import Author, Entry

admin.site.register(Author)

#admin.site.register(Entry, EntryAdmin) # instead of using this, you can use the decorator @admin, as seen below

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    # list_display controls what you see when you view a list of objects, eg when you click Entries, you will see the title, and these fields below
    list_display = ('title', 'author', 'date_created', 'date_published', )

    #fields = ('author', 'title', 'date_created', 'date_published')     # when editing the entry, you can limit the types of fields you see like this. 
    #exclude = ('author', ) # or alternatively you can have it include all fields, except for this exclude list.

    # You can also change the fields so that they group together with fieldsets
    '''fieldsets = (
        (None, {
            'fields': ('title', 'html_content',)
        }),
        ('dates', {
            'classes': ('collapse',),       # this means by default it's collapsed
            'fields': ('date_created', 'date_published'),
        }),
    )'''





