from django.shortcuts import render
from django.http import Http404
from .models import Entry
from django.utils import timezone

def home_page(request):
    return render(request, 'home.html')

def list_of_blog_posts(request):
    context = {'blog_post_list': Entry.objects.all().filter(date_published__lte=timezone.now())}
    return render(request, 'blog_entries.html', context)

def blog_post(request, blog_id):
    try: 
        #entry_ = Entry.objects.get(id=blog_id)
        entry_ = Entry.objects.filter(date_published__lte=timezone.now()).get(id=blog_id)
    except Entry.DoesNotExist:
        raise Http404("Blog post does not exist, or is set to private")
    else:
        context = {'blog_content': entry_}
        return render(request, 'blog_post.html', context)        

        
