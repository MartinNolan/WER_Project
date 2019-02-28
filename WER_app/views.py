from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'WER_app/index.html')


def search(request):
    return render(request, 'WER_app/search.html')

