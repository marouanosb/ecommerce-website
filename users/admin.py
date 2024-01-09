from django.contrib import admin
from .models import Profile, Wishlist, Cart

# Register your models here.
admin.site.register(Profile)
admin.site.register(Wishlist)
admin.site.register(Cart)