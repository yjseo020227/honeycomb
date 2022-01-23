from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('', load_properties, name = 'properties_main'),
    path('json/rentalnumber' , rental_number, name = "rental_number"), 
    path('add-rental/', addRental, name = "add_rental")
    ]
