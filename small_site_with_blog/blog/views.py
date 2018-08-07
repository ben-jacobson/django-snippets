from django.shortcuts import render
from .models import Entry#, Author

def home_page(request):
    return render(request, 'home.html')

def list_of_blog_posts(request):
    blog_post_list = Entry.objects.all()
    return render(request, 'blog_entries.html', {'blog_post_list': blog_post_list})

def blog_post(request, blog_id):
    return render(request, 'blog_post.html')
