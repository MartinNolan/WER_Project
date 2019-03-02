import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","WER_project.settings")

import django
django.setup()
from WER_app.models import Review, Page

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
    
    
    reviews = {"Paesano Pizza": {"pages": Paesano_Pizza},
                "Library Cafe": {"pages": Library_Cafe}}
    
    id = 0
    """
    for review, review_data in reviews.items():
        
        for p in review_data["pages"]:
            r = add_review(id, p["comment"], p["price"], p["quality"], p["atmosphere"])
            id+=1 
        
        
        print(r)
        print(review)
        add_page(r, review)
        r = ""
    """
    id = 0
    for review, review_data in reviews.items():
        for p in review_data["pages"]:
            r = (add_review(id, p["title"], p["comment"], p["price"], p["quality"], p["atmosphere"]))
            id+=1
           
        
        add_page(r, p["title"])
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
    
def add_page(review, title):
    p = Page.objects.get_or_create(title=title)[0]
    p.save()
    
if __name__ == '__main__':
    print("Starting WER_app population script...")
    populate()