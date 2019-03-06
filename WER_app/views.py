from django.shortcuts import render
from django.http import HttpResponse
from WER_app.models import Review, Page

def index(request):
    return render(request, 'WER_app/index.html')


def search(request):
    return render(request, 'WER_app/search.html')

def about(request):
    return render(request, 'WER_app/about.html')
    
    
def FAQ(request):
    return render(request, 'WER_app/FAQ.html')

def tAndC(request):
    return render(request, 'WER_app/t&cs.html')
    
def contact(request):
    return render(request, 'WER_app/contact-us.html')
    
def review_sample(request):
    review_list = Review.objects.order_by('reviewID')[:4] 
    pages = Page.objects.order_by('title')[:4]
    context_dict = {'reviews': review_list, 'pages':pages}

    return render(request, 'WER_app/review_sample.html', context_dict)




