from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

#this form below creates a new user, so you can add more fields in the list below if needed

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']
    
#this form below adds custom fields for the user to fill, so you can add more fields in the list below if needed

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        