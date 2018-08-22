from django.shortcuts import render_to_response
from .forms import CustomerForm

from django.http import HttpResponse

from django.views.generic.edit import FormView
from django.views.generic import DetailView

class home_page(FormView):
    template_name = 'home.html'
    form_class = CustomerForm
    
    def post(self, request):
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save() # this takes all data from the form and creates a new database object from it. This also automatically cleans/santizes the data 
            html_output = "Submitted the following form: <br /><br />"
            #for field in form.cleaned_data:    # form.cleaned_data is a python dictionary
            #    html_data += field + "<br />"
            return HttpResponse(html_output)
        else:
            return render_to_response(self.template_name, {'form': form})

class view_customer_details(DetailView):
    def get(self, request, cust_email):
        pass