from django.db import models

class Customer(models.Model):
    SALUTATION_CHOICES = (
        ('Master'),
        ('Mr'),
        ('Mrs'),
        ('Ms'),
        ('Miss'),
        ('Dr'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    salutation = models.CharField(max_length=8, choices=SALUTATION_CHOICES, help_text="Salutation", blank=True) 
    first_name = models.CharField(max_length=50, help_text="First Name")  
    middle_name = models.CharField(max_length=50, help_text="Middle Name", blank=True)  
    surname = models.CharField(max_length=50, help_text="Surname")  

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, help_text="Gender")
    dob = models.DateField(help_text="Date of Birth")

    email = models.EmailField(unique=True, help_text="Email Address")
    phone = models.BigIntegerField(help_text="Home Phone Number", blank=True)
    mobile = models.BigIntegerField(help_text="Mobile Phone Number", blank=True)

    address_1 = models.CharField(max_length=120, help_text="Address Line 1") 
    address_2 = models.CharField(max_length=120, help_text="Address Line 2", blank=True) 
    city = models.CharField(max_length=50, help_text="City") 
    state = models.CharField(max_length=50, help_text="State")
    country = models.CharField(max_length=50, help_text="Country")

    date_account_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):  # returns hte name by default
        fullname = self.first_name + " " + self.middle_name + " " + self.surname
        return fullname
    
    class Meta:
        ordering = ('-date_account_created',) # newest to oldest
