from django.db import models
from .countries import COUNTRIES
from django.urls import reverse

class Customer(models.Model):
    TITLE_CHOICES = (       # a sample size of 560K english speaking people living in the UK, finds that these 7 titles account for 99.6% of the population - https://www.codeproject.com/Questions/262876/Titles-or-Salutation-list 
        ('MR', 'Mr'),
        ('MRS', 'Mrs'),
        ('MS', 'Ms'),
        ('MISS', 'Miss'),
        ('DR', 'Dr'),
        ('PROF', 'Prof'),
        ('REV', 'Rev'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    title = models.CharField(max_length=4, choices=TITLE_CHOICES, blank=True) 
    first_name = models.CharField(max_length=50)  
    middle_name = models.CharField(max_length=50, blank=True)  
    surname = models.CharField(max_length=50)  

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(verbose_name="Date of birth")

    '''email_error_messages = {
        "blank": "This field cannot be empty",
        "invalid": "Please enter a valid email address",
        "unique": "We already have an account with that email address",
    }''' # my error messages aren't really that unique, will see what Django's ones are and use those. For learning purposes, will leave this code commented out in case I want to use it in a future project
    email = models.EmailField(unique=True)#, error_messages=email_error_messages)
    phone = models.BigIntegerField(verbose_name="Home phone number", blank=True, null=True)
    mobile = models.BigIntegerField(verbose_name="Mobile number", blank=True, null=True)

    address_1 = models.CharField(max_length=120) 
    address_2 = models.CharField(max_length=120, blank=True) 
    city = models.CharField(max_length=50) 
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=2, choices=COUNTRIES, default="Australia")

    date_account_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):  # returns the name by default
        fullname = self.first_name + " " + self.middle_name + " " + self.surname
        return fullname
    
    #def get_absolute_url(self):
    #   pass
    # get_absolute_url can be used in conjunction with generic views such as DetailView, to help the view output the models data to a template. Very efficient! 

    def get_success_url(self):
        return reverse('thanks_url', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('-date_account_created',) # newest to oldest
