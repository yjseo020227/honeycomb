from django.http.response import JsonResponse
from django.shortcuts import render,redirect 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import * 


# 1. Standard library imports.from math import sqrt and from os.path import abspath
# 2. Imports from core Django.from django.db import models and from django.utils.translation import gettext_lazy as _
# 3. Imports from third-party apps including those unrelated to Django.
#4. Imports from the apps that you created as part of your Django project. (You’ll read more about apps in
# Create your views here.

def dashboard(request):
    if request.method == 'GET':
        landlords_list = Landlord.objects.all()
        #property_list = Property.objects.all()
        name_to_filter = "yjseo0227"
        property_list = Property.objects.filter(landlord__username = name_to_filter)
        # you can pass a queryset into the context but you can't return this as a response.
        return render(request,'dashboard.html', {'properties': property_list , 'landlords':landlords_list })

def get_data(request):
    user = request.GET.get('user',None)
    print('user is '+ str(user))

    url_list = []
    property_list = Property.objects.filter(landlord__person__first_name = user)
    property_list_send = list(Property.objects.filter(landlord__person__first_name = user).values())
    count = 0 
    for property in property_list: 
        url = property.photos.url
        property_list_send[count]['photos'] = url
        count += 1
        
    # property_list now has valid urls 
    
    data = {'properties': property_list_send}
    return JsonResponse(data)




def cashflow(request):
    if request.method == 'GET':
        return render(request,'cashflow.html')

def payments(request):
    if request.method == 'GET':
        return render(request,'payments.html')

def upload_data(request):
    if request.method == 'GET':
        return render(request,'upload_data.html')