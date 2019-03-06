from django.db import models

# Create your models here.

#class UserProfile(models.Model):
#    user = models.OneToOneField(User)

class Review(models.Model):
   
    reviewID = models.IntegerField(unique=True)
    title = models.CharField(max_length=50, default="Default")
    #user
    
    comment = models.CharField(max_length=200, default="Default")  
    date = models.DateField(auto_now=True)
    price = models.IntegerField(default=0)
    quality = models.IntegerField(default=0)
    atmosphere = models.IntegerField(default=0)
    avgRating = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.reviewID)

        
class Page(models.Model): 
    title = models.CharField(max_length=128) 
    picture = models.FileField(upload_to="restaurant", null=True, blank=True) 
    description = models.CharField(max_length=128, default="Default")
    address = models.CharField(max_length=128, default="Default")
    openingHours = models.CharField(max_length=128, default="Default")
    
    def __str__(self): 
        return self.title
