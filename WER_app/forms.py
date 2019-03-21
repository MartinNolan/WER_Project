from django import forms
from WER_app.models import UserProfile, Review, Page
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    title = forms.CharField(widget=forms.HiddenInput(), initial="")
    comment = forms.CharField(max_length=128, help_text="Please enter a comment.")
    price = forms.IntegerField(help_text="Rate the price.")
    quality = forms.IntegerField(help_text="Rate the quality.")
    atmosphere = forms.IntegerField(help_text="Rate the atmosphere.")
    avgRating = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
    
    class Meta:
        model = Review
        fields = ('reviewID','title','comment','price','quality','atmosphere','avgRating',)
        
class Reviews(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('reviewID','title','comment','price','quality','atmosphere','avgRating',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
            model = UserProfile
            fields = ('picture',)



            
