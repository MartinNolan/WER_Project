from django import forms
from rango.models import UserProfile,Review



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('id', 'email','password', 'admin')
        
        
class Reviews(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('reviewID','title','comment','date','price','quality','atmosphere','avgRating;')