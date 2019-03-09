from django import forms
from WER_app.models import UserProfile, Review, Page
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class Reviews(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('reviewID','title','comment','price','quality','atmosphere','avgRating',)
