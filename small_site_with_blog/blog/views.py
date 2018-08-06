from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("home page")

def list_of_blog_posts(request):
    return HttpResponse("list of blog posts")

def blog_entry(request, blog_id):
    return HttpResponse("You're looking at blog post %s" % blog_id)
