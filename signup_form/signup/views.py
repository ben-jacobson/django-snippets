#from django.shortcuts import render
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
            # At this stage, should redirect to a new page 
            return HttpResponse("Thanks for submitting")
        else:
            html_data = "There was an error in the form: <br /><br />"
            for field in form.cleaned_data:
                html_data += field + "<br />"
            return HttpResponse(html_data)

class view_customer_details(DetailView):
    def get(self, request, cust_email):
        pass