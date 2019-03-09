from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.


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
    slug = models.SlugField(blank=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
        
        
    def __str__(self): 
        return self.title
    
class UserProfile(models.Model):
# This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
# Override the __unicode__() method to return out something meaningful!
# Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username
