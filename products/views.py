from django.shortcuts import render
from django.http import HttpResponse
from .models import product

# Create your views here.
def index(request):
    products = product.objects.all()
    return render(request,'index.html',{'products':products})
    return HttpResponse("<h1>Welcome to django</h>")

def about(request):
    return HttpResponse("<h1>about page</h>")   

def contact(request):
    return HttpResponse("<h1>contact page</h>")     
