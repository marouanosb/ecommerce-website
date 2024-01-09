from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('produit', views.product, name='product'),
    path('recherche', views.search, name='search'),
    path('ajout_produit', views.addproduct, name='addproduct'),
]
