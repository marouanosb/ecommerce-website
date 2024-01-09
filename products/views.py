from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'products/homepage.html')

def product(request):
    return render(request, 'products/product.html')

def search(request):
    return render(request, 'products/search.html')

def addproduct(request):
    return render(request, 'products/addproduct.html')