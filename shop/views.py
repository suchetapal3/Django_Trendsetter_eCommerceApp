from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    #products = Product.objects.all()
         
    #n = len(products)
    #nSlides = n//4 + ceil((n/4)-(n//4))
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    #params={'no_of_slides': nSlides, 'range': range(nSlides), 'product': products}
    #allProds = [[products, range(1, nSlides), nSlides],[products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request): 
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at Contact")

def tracker(request):
    return HttpResponse("We are at Tracker")

def search(request):
    return HttpResponse("We are at Search")

def prodView(request):
    return HttpResponse("We are at Product View")

def checkout(request):
    return HttpResponse("We are at checkout")
