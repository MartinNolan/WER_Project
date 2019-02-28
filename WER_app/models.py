from django.db import models

# Create your models here.

#class UserProfile(models.Model):
#    user = models.OneToOneField(User)

class Review(models.Model):
   
    reviewID = models.IntegerField(unique=True)
    #user
    date = models.DateField(auto_now=True)
    comment = models.CharField(max_length=200, default="Default")  
    price = models.IntegerField(default=0)
    quality = models.IntegerField(default=0)
    atmostphere = models.IntegerField(default=0)
    avgRating = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.reviewID)
