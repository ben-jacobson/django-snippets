#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import redirect
from signin.models import Superhero
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse

class home_page(LoginView):
    template_name = 'home.html'

#Commented out ar the method_decorators for login required, they've since been refactored to use a mixin.

#@method_decorator(login_required, name='dispatch')       #  see below for alternative ways to do this. 
class superhero_listView(LoginRequiredMixin, ListView):  
    #login_url = '/login/'      # these can be customized, or you could specify them in settings.py
    #redirect_field_name = 'redirect_to'
    template_name = 'superhero_listview.html'  
    context_object_name = 'superhero_list'

    def get_queryset(self):
        return Superhero.objects.all()

#@method_decorator(login_required, name='dispatch')   # you can even specify - permission_required=
class superhero_detailView(LoginRequiredMixin, DetailView):
    template_name = 'superhero_detailview.html'
    model = Superhero

    def dispatch(self, *args, **kwargs):
        if self.request.user.has_perm('signin.change_superhero'):
            self.object = self.get_object(queryset=self.queryset) # Because we haven't run the get method, the self.object isn't populated, this generates it for us in case we need it. or can use self.object = super(DetailView, self).get_object(queryset=queryset)
            return redirect(self.object.get_edit_url())
        return super().dispatch(*args, **kwargs)

#@method_decorator(login_required, name='dispatch')
class superhero_editView(PermissionRequiredMixin, UpdateView):  # when using PermissionRequiredMixin, you don't need to use the LoginRequiredMixin as well
    permission_required = 'signin.change_superhero'

    template_name = 'superhero_editview.html'
    model = Superhero    
    fields = [
        'name', 
        'bio',
        'picture',
    ]

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)       # get the usual 'object' context data, so that we can append to it.
        context_data['user_has_delete_permissions'] = self.request.user.has_perm('signin.delete_superhero')
        return context_data

    def get_success_url(self):      # UpdateView will make use of get_absolute_url, and in this case the model sets this to the view page - in our app it redirects if you have the correct permission, but that's 3 page loads instead of 1. 
        return self.object.get_edit_url()   # important to note that you can only call the object member after get, since this creates it for us via get_context

    #def has_permissions(self):       # you can manually check permission checks this way, although it's cleaner to use a mixin
    #    #return self.request.user.has_perm('signin.change_superhero') 
    #    return False  

#@method_decorator(login_required, name='dispatch')
class superhero_deleteView(PermissionRequiredMixin, DeleteView):
    model = Superhero
    permission_required = 'signin.delete_superhero'
    template_name = 'superhero_deleteview.html'

    def get_success_url(self):
        return reverse('superhero_listview')

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