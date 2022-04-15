from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class createuser(UserCreationForm):
    password1 = forms.CharField(label='',required = False,widget = forms.HiddenInput(),)
    password2=forms.CharField(label='',required = False,widget = forms.HiddenInput())
    # passwordd = forms.CharField(label='Confirm Password')
    email=forms.EmailField(required=True)
    first_name=forms.CharField(label = "Password",required=True,widget=forms.PasswordInput)
    last_name=forms.CharField(required=True,label = "Confirm Password",widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

    def clean(self):
        super(createuser, self).clean()
        # This method will set the `cleaned_data` attribute

        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if not first_name == last_name:
            self.add_error('first_name', 'Please Enter E-Mail Credentials')
            raise forms.ValidationError('<h1>Passwords must match</h1>')

    # def form_valid(self):
    #     if not self.first_name == self.last_name:
    #         print("both are not the same=============")
    #         raise forms.ValidationError("Headline must be more than 5 characters.")

class loginform(forms.Form):
    username=forms.CharField(max_length=122,required=True)
    password=forms.CharField(max_length=122,widget=forms.PasswordInput,required=True)