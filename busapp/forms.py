import re
from django import forms
<<<<<<< HEAD
=======
from django.forms.widgets import *
>>>>>>> arora
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="Username" )
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="Email address")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label= "Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label= "Password (again)")

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
<<<<<<< HEAD
        return self.cleaned_data
=======
        return self.cleaned_data

class BusQueryForm(forms.Form):
    def setplaces(sources,destinations):
	source=forms.ChoiceField(widget=forms.Select, choices=sources)
	destination=forms.ChoiceField(widget=forms.Select, choices=destinations)
	date = forms.DateField(widget=SelectDateWidget)
>>>>>>> arora
