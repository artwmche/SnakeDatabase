from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Snake


class SnakeForm(ModelForm):
  class Meta:
    model = Snake
    fields = ['name', 'description','color_or_pattern','favourite_prey','region','venomous']



#class UserCreationForm(UserCreationForm):
#    username = forms.CharField(max_length=20)
#    password = forms.CharField(widget=forms.PasswordInput)
#    passwordConfirm = forms.CharField(widget=forms.PasswordInput)
#    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
