#from django.forms import ModelForm
#from .models import Customer

'''class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        #exclude = ['date_account_created', 'title']      # not technical necessary to exclude date_account_created since this field is set to editable=false. Simply wanted to demonstrate this functionality
'''        
''' # alternatively, can manually enter all of the fields you want to use,         
        fields = [
            'title', 
            'first_name',
            ...
        ]
'''