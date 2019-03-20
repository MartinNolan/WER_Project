from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.


class Review(models.Model):
   
    reviewID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="Default")
    #user
    
    comment = models.CharField(max_length=200, default="Default")  
    date_modified = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    quality = models.IntegerField(default=0)
    atmosphere = models.IntegerField(default=0)
    avgRating = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.reviewID)

    def save(self, *args, **kwargs):
        self.avgRating = (self.price + self.quality + self.atmosphere)/3 
        super(Review, self).save(*args, **kwargs)
        
class Page(models.Model): 

    title = models.CharField(max_length=128) 
    picture = models.FileField(upload_to="restaurant", null=True, blank=True) 
    description = models.CharField(max_length=128, default="Default")
    address = models.CharField(max_length=128, default="Default")
    openingHours = models.CharField(max_length=128, default="Default")
    longitude = models.DecimalField(max_digits=15, decimal_places=10, default = 0)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, default = 0)
    onCampus = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
        
        
    def __str__(self): 
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
