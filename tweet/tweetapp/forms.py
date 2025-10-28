from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    #tells django how to configure form 
    class Meta:
        model=Tweet
        fields=['text','photo']

        #dont mention all the fields only required
