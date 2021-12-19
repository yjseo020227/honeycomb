from django.shortcuts import render
from .models import Property
from accounts.models import Landlord

# Create your views here.
def load_properties(request):
    if request.user.is_authenticated:
        user = request.user
        username = user.username
        print(username)
        properties = Property.objects.filter(landlord__username = username)
        print(properties)
        return render(request, 'properties.html' , context = {'properties': properties})

        