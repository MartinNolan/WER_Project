from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    return HttpResponse("This is West End Restaurants! <br/> <a href='/WER_app/about/'>About</a> ")
    

def about(request):
    return HttpResponse("About Us")
