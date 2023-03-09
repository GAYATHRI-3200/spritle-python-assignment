from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
class contactForm(forms.Form): #new form called contactForm
    Username = forms.CharField(required=True,max_length=50)
    UserEmail = forms.EmailField(required=True)
    Message = forms.CharField(required=True,widget=forms.Textarea)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
            ]

