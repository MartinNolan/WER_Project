import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","WER_project.settings")

import django
django.setup()
from WER_app.models import Review, Page
from django.core.files import File
import os
import glob

"""
Review entity template
[
        {"title":"title",
         "comment":,
         "price":,
         "quality":,
         "atmosphere":,}]
"""

def populate():
    cwd = os.getcwd()
    files = glob.glob(cwd+'/media/restaurant/*')
    for f in files:
        os.remove(f)
    
    Paesano_Pizza = [{"title":"Paesano Pizza",
         "comment":"Great Pizza",
         "price":4,
         "quality":5,
         "atmosphere":4 },
         {"title":"Paesano Pizza",
         "comment":"Bad Pizza",
         "price":4,
         "quality":1,
         "atmosphere":3 }]
    Library_Cafe = [{"title":"Library Cafe",
         "comment":"Easy and fast but quite expensive",
         "price":2,
         "quality":4,
         "atmosphere":4},
         {"title":"Library Cafe",
         "comment":"Nothing interesting to eat but nice place",
         "price":3,
         "quality":2,
         "atmosphere":4}]
    Ubiquitous_Chip = [{"title":"Ubiquitous Chip",
         "comment":"Fancy and very nice",
         "price":4,
         "quality":5,
         "atmosphere":4},
         {"title":"Ubiquitous Chip",
         "comment":"Good food but pretentious name",
         "price":3,
         "quality":5,
         "atmosphere":2}]
    
    
    reviews = {"Paesano Pizza": {"pages": Paesano_Pizza, "image":"Paesano_Pizza.jpg", "description":"Pizza Place", "address":"471 Great Western Road, Glasgow G12 8HL, Scotland", "openingHours":"Sun - Wed  12:00 - 22:30\nThu 12:00 - 23:00\nFri12:00 - 00:00"},
                "Library Cafe": {"pages": Library_Cafe, "image":"Library_Cafe.jpg", "description":"Cafe in the University Library", "address":"University of Glasgow, Hillhead St, Glasgow G12 8QE", "openingHours":"Mon- Thu: 10:00 - 20:00\nFri: 10:00 - 17:00\nSat/Sun: 10:30 - 17:00"},
                "Ubiquitous Chip": {"pages": Ubiquitous_Chip, "image":"Ubiquitous_Chip.jpg", "description":"Fancy food place", "address":"12 Ashton Lane, Glasgow G12 8SJ, Scotland", "openingHours":"Sun – Sat 11:00 - 01:00"}}
    
    id = 0
    for review, review_data in reviews.items():
        for p in review_data["pages"]:
            r = (add_review(id, p["title"], p["comment"], p["price"], p["quality"], p["atmosphere"]))
            id+=1
           
        
        add_page(r, p["title"], review_data["image"] , review_data["description"], review_data["address"], review_data["openingHours"])
    #print(str(r))
        
        
    for r in Review.objects.all(): 
         print(str(r))

    
def add_review(reviewID, title, comment, price, quality, atmosphere):
    r = Review.objects.get_or_create(reviewID=reviewID)[0]
    #date = current date
    r.title=title
    r.comment = comment  
    r.price = price
    r.quality = quality
    r.atmosphere = atmosphere
    r.avgRating = (price+quality+atmosphere)/3
    r.save()
    return r
    
def add_page(review, title, image, description, address, openingHours):
    p = Page.objects.get_or_create(title=title)[0]
    cwd = os.getcwd()
    pic_dir = cwd+'/media/'+image
    p.picture.save(image, File(open(cwd+'/media/'+image, 'rb')))
    p.description = description
    p.address = address
    p.openingHours = openingHours
    p.save()
    
if __name__ == '__main__':
    print("Starting WER_app population script...")
    populate()