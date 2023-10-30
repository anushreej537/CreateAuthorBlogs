from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, EmailInput,PasswordInput
class SignupForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter confirm password'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name'}
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter username'
                }),
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter First_Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter Last_Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Enter Email'
                }),
          
         }