from django.shortcuts import render
from .forms import CustomerForm

def home_page(request):
    form = CustomerForm()
    return render(request, 'home.html', {'form': form})