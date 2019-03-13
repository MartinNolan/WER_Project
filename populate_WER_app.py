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
         "atmosphere":2},
         {"title":"Ubiquitous Chip",
         "comment":"Food was subpar but the name was very interesting",
         "price":3,
         "quality":2,
         "atmosphere":3}]
    Food_for_Thought = [
        {"title":"Food for Thought",
         "comment":"Nice place but not open very long",
         "price":4,
         "quality":4,
         "atmosphere":3}]
    Food_to_Go = [
        {"title":"Food to Go",
         "comment":"Very nice and excellent sandwiches",
         "price":4,
         "quality":4,
         "atmosphere":5}]
    Cafe_Piccolino = [
        {"title":"Cafe Piccolino",
         "comment":"Friendly and helpful staff",
         "price":4,
         "quality":4,
         "atmosphere":3},
         {"title":"Cafe Piccolino",
         "comment":"My grandson Freddie brought me here today as I am visiting him from Edinburgh, it was so nice to spend time with him and talk to him over lunch. Toastie a bit cold but my heart was warm and happy.",
         "price":4,
         "quality":3,
         "atmosphere":4}]
    Food_in_Focus = [
         {"title":"Food in Focus",
         "comment":"Friendly and helpful staff",
         "price":4,
         "quality":4,
         "atmosphere":3}]
    
    
    reviews = {"Paesano Pizza": {"pages": Paesano_Pizza, "image":"Paesano_Pizza.jpg", "description":"Pizza Place", "address":"471 Great Western Road, Glasgow G12 8HL, Scotland", "openingHours":"Sun - Wed  12:00 - 22:30\nThu 12:00 - 23:00\nFri12:00 - 00:00", "onCampus":False},
                "Library Cafe": {"pages": Library_Cafe, "image":"Library_Cafe.jpg", "description":"Cafe in the University Library", "address":"University of Glasgow, Hillhead St, Glasgow G12 8QE", "openingHours":"Mon- Thu: 10:00 - 20:00\nFri: 10:00 - 17:00\nSat/Sun: 10:30 - 17:00", "onCampus":True},
                "Ubiquitous Chip": {"pages": Ubiquitous_Chip, "image":"Ubiquitous_Chip.jpg", "description":"Fancy food place", "address":"12 Ashton Lane, Glasgow G12 8SJ, Scotland", "openingHours":"Sun – Sat 11:00 - 01:00", "onCampus":False},
                "Food for Thought": {"pages": Food_for_Thought, "image":"Food_for_Thought.jpg", "description":"Cafe in the Fraser Building for students, staff and visitors to the campus, serving hot meals and snacks.", "address":"Fraser Building, 65 Hillhead St, Glasgow G12 8QF", "openingHours":"Mon-Fri 11:00 - 15:00 ","onCampus":True},
                "Food to Go": {"pages": Food_to_Go, "image":"Food_for_Thought.jpg", "description":"Offers everything you need for breakfast on the go, lunch on the run or an eveningsnack to sustain you during late study sessions.", "address":"Fraser Building, 65 Hillhead St, Glasgow G12 8QF", "openingHours":"Mon-Thu 08:00 - 18:00, Fri 08:00 - 16:30", "onCampus":True},
                "Cafe_Piccolino": {"pages": Cafe_Piccolino, "image":"Cafe_Piccolino.jpg", "description":"Proud to serve Orang Utan coffee supporting an important Sumatran conservation project", "address":"Ashton Ln, Glasgow G12 8QR", "openingHours":"Mon-Fri 08:30 - 15:00 ", "onCampus":True},
                "Food in Focus": {"pages": Food_in_Focus, "image":"Food_in_Focus.jpg", "description":"Comfy seating in a newly decorated area for library users and vending machines accessible during library opening hours", "address":"University of Glasgow, Hillhead St, Glasgow G12 8QE", "openingHours":"Mon- Thu: 10:00 - 20:00\nFri: 10:00 - 17:00\nSat/Sun: 10:30 - 17:00", "onCampus":True},
                "Food for Thought": {"pages": Food_for_Thought, "image":"Food_for_Thought.jpg", "description":"Cafe in the Fraser Building for students, staff and visitors to the campus, serving hot meals and snacks.t", "address":"Fraser Building, 65 Hillhead St, Glasgow G12 8QF", "openingHours":"Mon-Fri 11:00 - 15:00 ", "onCampus":False}}
                


    for review, review_data in reviews.items():
        for p in review_data["pages"]:
            r = (add_review(p["title"], p["comment"], p["price"], p["quality"], p["atmosphere"]))
           
        
        add_page(r, p["title"], review_data["image"] , review_data["description"], review_data["address"], review_data["openingHours"], review_data["onCampus"])

        
        
    for r in Review.objects.all(): 
         print(str(r))

    
def add_review(title, comment, price, quality, atmosphere):
    r = Review.objects.create()
    #date = current date
    r.title=title
    r.comment = comment  
    r.price = price
    r.quality = quality
    r.atmosphere = atmosphere
    r.avgRating = (price+quality+atmosphere)/3
    r.save()
    return r
    
def add_page(review, title, image, description, address, openingHours, onCampus):
    p = Page.objects.get_or_create(title=title)[0]
    cwd = os.getcwd()
    pic_dir = cwd+'/media/'+image
    p.picture.save(image, File(open(cwd+'/media/'+image, 'rb')))
    p.description = description
    p.address = address
    p.openingHours = openingHours
    p.onCampus = onCampus
    p.save()
    
if __name__ == '__main__':
    print("Starting WER_app population script...")
    populate()