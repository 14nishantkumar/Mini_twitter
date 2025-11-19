from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['title','text','photo','video']
    def clean(self):
        cleaned_data= super().clean()
        photo=cleaned_data.get('photo')
        video=cleaned_data.get('video')
        if photo and video:
            raise forms.ValidationError("You can upload either a photo or a video, not both.")
        return cleaned_data

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=('username','email','password1','password2')