from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'users/register.html')

def profile(request):
    return render(request, 'users/profile.html')

def wishlist(request):
    return render(request, 'users/whislist.html')

def cart(request):
    return render(request, 'users/cart.html')