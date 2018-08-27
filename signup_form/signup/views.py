#from django.shortcuts import render_to_response
#from .forms import CustomerForm

#from django.http import HttpResponse

#from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from .models import Customer

class home_page(CreateView):            # create view makes this easy since it will create the form for you. 
    template_name = 'home.html'
    model = Customer
    fields = '__all__'

    def get_success_url(self):
        return self.object.get_success_url()        # self.object refers to the instance of self.model. in this case Customer

class thanks(DetailView):
    template_name = 'thanks.html'
    model = Customer 
    context_object_name = 'customer_data'

'''class home_page(FormView):       # However if doing this manually, you'll need to use the FormView. Hint - this makes it easier to test because the unit tests can make copies of the form. 
    template_name = 'home.html'
    form_class = CustomerForm
    
    def post(self, request):
        form_data = CustomerForm(request.POST)

        # below is not something you'd have in a production environment. This is just to show how to get access to some of the data if ever necessary
        if form_data.is_valid():
            form_data.full_clean() # this method is not called prior to save, we need to manually call it prior to save()
            form_data.save() # this takes all data from the form and creates a new database object from it. This also automatically cleans/santizes the data 
            html_output = "Submitted the following form: <br /><br />"

            for key in form_data.cleaned_data.keys():
                html_output += f'{key}: {form_data.cleaned_data[key]}<br />'

            return HttpResponse(html_output)
        else:
            return render_to_response(self.template_name, {'form': form_data})'''
