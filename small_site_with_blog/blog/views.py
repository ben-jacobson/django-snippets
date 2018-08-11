from django.shortcuts import render
from .models import Entry#, Author
from datetime import datetime

def home_page(request):
    return render(request, 'home.html')

def list_of_blog_posts(request):
    context = {'blog_post_list': Entry.objects.all().filter(date_published__lte=datetime.today())}
    return render(request, 'blog_entries.html', context)

def blog_post(request, blog_id):
    context = {'blog_content': Entry.objects.get(id=blog_id)}
    return render(request, 'blog_post.html', context)
