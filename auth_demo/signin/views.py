from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from django.views.generic.edit import FormView
from .forms import LoginForm

#from django.views import View
#from django.shortcuts import redirect
from django.shortcuts import render, render_to_response

class home_page(FormView):       # However if doing this manually, you'll need to use the FormView. Hint - this makes it easier to test because the $
    template_name = 'home.html'
    form_class = LoginForm
    
    def post(self, request):
        form_data = LoginForm(request.POST)

        # below is not something you'd have in a production environment. This is just to show how to get access to some of the data if ever necessary
        if form_data.is_valid():
            form_data.full_clean() # this method is not called prior to save, we need to manually call it prior to save()
            return render(request, self.template_name)
        else:
            return render_to_response(self.template_name, {'form': form_data})

# there are a couple of ways of requiring logins for pages, this is the raw way. With this method decorator, it relies on some settings within Settings.py - see comments near LOGIN_URL
@method_decorator(login_required, name='dispatch')       #  see below for alternative ways to do this. 
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

#class home_page(TemplateView):
#    template_name = 'home.html'