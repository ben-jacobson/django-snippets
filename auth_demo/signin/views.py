from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from signin.models import Superhero

class home_page(LoginView):
    template_name = 'home.html'

# there are a couple of ways of requiring logins for pages, this is the raw way. With this method decorator, it relies on some settings within Settings.py - see comments near LOGIN_URL
@method_decorator(login_required, name='dispatch')       #  see below for alternative ways to do this. 
class superhero_listView(ListView):  
    template_name = 'superhero_listview.html'  
    context_object_name = 'superhero_list'

    def get_queryset(self):
        return Superhero.objects.all()

@method_decorator(login_required, name='dispatch')   # you can even specify - permission_required=
class superhero_detailView(DetailView):
    template_name = 'superhero_detailview.html'
    model = Superhero

## Old code that has since been refactored
'''class home_page(FormView):       # Delete this, once we have something that works
    template_name = 'home.html'
    form_class = LoginForm
    
    def post(self, request):
        form_data = LoginForm(request.POST)

        context = {
            'form': form_data,
            'error_message': ''
        }        

        # below is not something you'd have in a production environment. This is just to show how to get access to some of the data if ever necessary
        if form_data.is_valid():
            form_data.full_clean() # unsure if this is needed because we aren't saving a ModelForm, will keep just in case. 
            username = request.POST['email_username']
            password = request.POST['password']
            user_ = authenticate(request, username=username, password=password)

            if user_ is not None: # if user has been logged in
                login(request, user_)
                return redirect(reverse('superhero_listview')) 
            else:               # if user doesn't exist in database
                context['error_message'] = "Username and/or password was incorrect"
                return render_to_response(self.template_name, context)
        else:
            return render_to_response(self.template_name, context)'''


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