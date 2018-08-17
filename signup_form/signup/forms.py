from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'title', 
            'first_name',
            'middle_name',
            'surname',
            'gender',
            'dob',
            'email',
            'phone',
            'mobile',
            'address_1',
            'address_2',
            'city',
            'state',
            'country',
        ]