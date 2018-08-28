from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

#from django.views import View
#from django.shortcuts import render
#from django.shortcuts import redirect

class home_page(TemplateView):
    template_name = 'home.html'

# there are a couple of ways of requiring logins for pages, this is the raw way

@method_decorator(login_required, name='dispatch')       #  see below for alternative ways to do this
class superhero_listView(TemplateView):  
    template_name = 'superhero_listview.html'  

@method_decorator(login_required, name='dispatch')   # you can even specify - permission_required=
class superhero_detailView(TemplateView):
    template_name = 'superhero_detailview.html'


'''def superhero_listView(request):
    if not request.user.is_authenticated:
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        return redirect('/')
    else:
        return render(request, 'superhero_listview.html')'''

'''@login_required      # this is a function based view using the decorator - login_required
def superhero_listView(request):
    return render(request, 'superhero_listview.html')'''
    
'''class superhero_listView(View):
    template_name = 'superhero_listview.html'

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)
'''