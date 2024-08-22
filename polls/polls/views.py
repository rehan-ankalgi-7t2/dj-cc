from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World, your are at chai aur django home page")
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

