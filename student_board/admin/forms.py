from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from register.models import Admin


class addAdminForm(forms.Form):
    id=forms.CharField(label='id', max_length=10)
    first_name=forms.CharField(label='first name', max_length=20)
    last_name=forms.CharField(label='last name', max_length=20)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password')


