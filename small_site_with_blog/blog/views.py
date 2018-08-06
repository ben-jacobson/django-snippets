from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def list_of_blog_posts(request):
    return render(request, 'blog_entries.html')

def blog_entry(request, blog_id):
    return render(request, 'blog_post.html')
