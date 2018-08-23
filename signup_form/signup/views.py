from django.shortcuts import render_to_response
from .forms import CustomerForm

from django.http import HttpResponse

from django.views.generic.edit import FormView
from django.views.generic import DetailView

class home_page(FormView):
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
            return render_to_response(self.template_name, {'form': form_data})

class view_customer_details(DetailView):
    def get(self, request, cust_email):
        pass