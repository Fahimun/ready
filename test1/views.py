from django.shortcuts import render
from django.http import HttpRequest
from .models import *


# Create your views here.
def home(request):
    return render(request, 'test1/home.html')

def save(request):
    return render(request, 'test1/contact.html')

def contact(request):
    contact = Contact.objects.all()
    
    
    context = {
        'cn':contact
    }
  # print(type (contact))
    return render(request,'test1/contact.html',context)
def detail(request):
    return render(request, 'test1/detail.html')

