from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('', load_properties, name = 'properties_main'),
    ]
