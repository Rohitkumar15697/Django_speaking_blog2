from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class createuser(UserCreationForm):
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    email=forms.EmailField(required=True)
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']

class loginform(forms.Form):
    username=forms.CharField(max_length=122,required=True)
    password=forms.CharField(max_length=122,widget=forms.PasswordInput,required=True)