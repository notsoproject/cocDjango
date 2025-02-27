from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['phone_number', 'email', 'password1', 'password2','playerTag']