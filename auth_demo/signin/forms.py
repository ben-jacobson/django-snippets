from django import forms

class LoginForm(forms.Form):
    email_username = forms.CharField(label='email address', max_length=255)
    password = forms.CharField(label='password', max_length=255)  