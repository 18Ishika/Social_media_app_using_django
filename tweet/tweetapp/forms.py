from django import forms
from .models import Tweet

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TweetForm(forms.ModelForm):
    #tells django how to configure form 
    class Meta:
        model=Tweet
        fields=['text','photo']

        #dont mention all the fields only required
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:   #metadata like how should it behave
        model=User
        fields=('username','email','password1','password2')

