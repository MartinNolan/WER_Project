from django.db import models
from django.template.defaultfilters import slugify

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
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)


    def __str__(self): 
        return self.title
    
class UserProfile(models.Model):
    userId = models.IntegerField(unique=True)
    email = models.CharField(max_length = 100, default="Defualt", unique=True)
    password = models.CharField(max_length = 30, default="Default")
    admin = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.userId)
