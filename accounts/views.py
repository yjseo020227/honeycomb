from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import render,redirect 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


from .forms import NewUserForm 
from .models import * 

from honeycomb import views as honeycombviews


# 1. Standard library imports.from math import sqrt and from os.path import abspath
# 2. Imports from core Django.from django.db import models and from django.utils.translation import gettext_lazy as _
# 3. Imports from third-party apps including those unrelated to Django.
#4. Imports from the apps that you created as part of your Django project. (You’ll read more about apps in
# Create your views here.
def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect(honeycombviews.dashboard)
        print('form is not valid')
        print(form.errors)
        #form.non_field_errors()
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            print('form is valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username = username , password = password)
            #authenticate returns a user obejct 
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {user.first_name}.")
                #print('user is not none')
                return redirect(honeycombviews.dashboard)
            else:
                messages.error(request,"Invalid username or password.")
        else:
            print('form is not valid')
            print(form.errors)
            form.non_field_errors()
            messages.error(request, "Invalid username or password.")
            
        
    
    form = AuthenticationForm()
    return render(request, 'loginn.html' , context = {"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")

def chooseSignUp(request):
    return render(request, 'signup_general.html')

def landlordSignUp(request):
    pass

def tenantSignUp(request):
    pass


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