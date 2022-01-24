from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse

from .forms import PropertyForm, SingleUnitForm
from .models import Property, SingleRentalUnit
from accounts.models import Landlord

# Create your views here.
def load_properties(request):
    if request.user.is_authenticated:
        user = request.user

        #POST request
        if request.method == 'POST':
            # add property
            if 'add_property' in request.POST:
                form = PropertyForm(request.POST, request.FILES)
                if form.is_valid(): 
                    property_instance = form.save(commit = False)
                    property_instance.landlord = user
                    property_instance.save()
                    messages.success(request, "Added Successfully")
                    single_unit_form = SingleUnitForm()
                    number_of_rentals = property_instance.number_of_rentals
                    request.session['property'] = property_instance.id
                    context = {'single_unit_form': single_unit_form, 'rentals': number_of_rentals}
                    return render(request, 'single_rental.html', context)
                else: 
                    print('form is not valid')
                    print(form.errors)
                    messages.error(request, "Unsuccessful registration. Invalid information.")
            # add single rental unit
            """elif 'add_single_unit' in request.POST: 
                form = SingleUnitForm(request.POST)
                if form.is_valid(): 
                    singleunit_instance = form.save(commit = False)
                    singleunit_instance.property = request.session['property']
                    empty_form = SingleUnitForm()"""


                    


        #get request
        else:  
            username = user.username
            properties = Property.objects.filter(landlord__username = username)
                
            # if there is no post request just render the form 
            property_form = PropertyForm()
            single_unit_form = SingleUnitForm()
            context = {'property_form' : property_form, 'properties' : properties, 'single_unit_form': single_unit_form}
            return render(request, 'properties.html',context)

def addProperties(request):
    pass

def addRental(request):
    if request.method == 'POST' and request.is_ajax: 
        form = SingleUnitForm(request.POST)
        if form.is_valid():
            # save the individual unit object to the db 
            single_rental_instance = form.save(commit = False) 
            property_id = request.session['property']
            property = Property.objects.get(id = property_id)
            single_rental_instance.property = property
            single_rental_instance.save()
            ser_instance = serializers.serialize("json", [single_rental_instance,])

            #figure out how many individual properties are left to add
            total_single_rentals = property.number_of_rentals 
            registered_single_rentals = SingleRentalUnit.objects.filter(property = property).count()
            left_to_register = str(total_single_rentals - registered_single_rentals)
            add_more = True
            if left_to_register == '0': 
                add_more = False
            
            return JsonResponse({"instance": ser_instance, "add_more":add_more , "left_to_register": left_to_register }, status=200)
        else: 
            return JsonResponse({"error": form.errors }, status = 400)
    #some other error
    return JsonResponse({"error": ""}, status = 400)
        

def addProperty(request):
    if request.user.is_authenticated:
        user = request.user
        username = user.username
        properties = Property.objects.filter(landlord__username = username)
        print(properties)
        if request.method == 'POST' and request.is_ajax:
            form = PropertyForm(request.POST, request.FILES)
            if form.is_valid():
                property = form.save( commit = False )
                property.landlord = user
                property.save()
                messages.success(request, "Added Successfully")
                property_instance = serializers.serialize('json', [ property, ])
                return JsonResponse({"instance": property_instance}, status=200)
                return redirect(load_properties)
            else: 
                return JsonResponse({"error": form.errors}, status=400)
        return JsonResponse({"error":""}, status = 400)
    

def rental_number(request):
    print('ajax request recieved')
    return JsonResponse({"number": 3}, status = 200)