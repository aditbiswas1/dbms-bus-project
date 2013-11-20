import re
from django import forms

from django.forms.widgets import *

from django.contrib.auth.models import User

from models import Company

class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="Username" )
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="Email address")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label= "Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label= "Password (again)")
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=(('1','company',),('2','customer',)),label = 'Type of User')
	
	
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError( "The username already exists. Please try another one.")

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError( "The two password fields did not match.")

        return self.cleaned_data
		
class CompanyForm(forms.Form):
    name = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="Company Name" )
    account_number = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=10)), label="Bank Account Number")
    manager_phone = forms.IntegerField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label= "Manager Phone No.")
	
	
    def clean_username(self):
        try:
            user = Company.objects.get(name__iexact=self.cleaned_data['name'])
        except Company.DoesNotExist:
            return self.cleaned_data['name']
        raise forms.ValidationError( "The company name already exists. Please try another one.")
		
class CustomerForm(forms.Form):
    fname = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="First Name" )
    lname = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="Last Name" )
    phone = forms.IntegerField(widget=forms.TextInput(attrs=dict(required=True, max_length=10)), label="Phone Number")
    bank = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=10)), label= "Bank Account No.")
    address = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label= "Address")
    dob = forms.DateField(widget=forms.TextInput(attrs=dict(required=True, max_length=10)), label="Date of Birth(YYYY-MM-DD)")
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=(('1','Male',),('2','Female',)),label = 'Gender')

class BusQueryForm(forms.Form):
    def setplaces(sources,destinations):
	source=forms.ChoiceField(widget=forms.Select, choices=sources)
	destination=forms.ChoiceField(widget=forms.Select, choices=destinations)
	date = forms.DateField(widget=SelectDateWidget)

