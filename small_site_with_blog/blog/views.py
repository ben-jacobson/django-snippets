from django.shortcuts import render
from django.http import Http404
from .models import Entry
from django.utils import timezone

from django.views import View
from django.views.generic import ListView

class home_page(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

'''class list_of_blog_posts(View):
    template_name = 'blog_entries.html'

    def get(self, request):
        context = {'blog_post_list': Entry.objects.all().filter(date_published__lte=timezone.now())}
        return render(request, self.template_name, context)
''' # see below how this has been refactored to use a generic ListView

class list_of_blog_posts(ListView):
    queryset = Entry.objects.all().filter(date_published__lte=timezone.now())
    context_object_name = 'blog_post_list'
    template_name = 'blog_entries.html'

'''class blog_post(View):
    template_name = 'blog_post.html'

    def get(self, request, blog_id):
        try: 
            entry_ = Entry.objects.filter(date_published__lte=timezone.now()).get(id=blog_id)
        except Entry.DoesNotExist:
            raise Http404("Blog post does not exist, or is set to private")
        else:
            context = {'blog_content': entry_}
            return render(request, self.template_name, context)'''

class blog_post(ListView):      # WIP
    context_object_name = 'blog_content'
    template_name = 'blog_post.html'

    def get_queryset(self):
        return(Entry.objects.filter(date_published__lte=timezone.now()).get(id=self.kwargs['blog_id']))

    


        
