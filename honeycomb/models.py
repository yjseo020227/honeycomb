from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.utils.translation import gettext_lazy as _ 

from accounts.models import Landlord

class Property(models.Model):
    landlord = models.ForeignKey(Landlord,on_delete=models.CASCADE)
    address = models.CharField(max_length = 500)
    name = models.CharField(max_length = 500)
    photos = models.ImageField()
    recent_price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_owner(self):
        return self.landlord.person.first_name
    
    
    def setPrice(self , price):
        self.recent_price = price

    class Admin:
        pass

"""class Property_Photos(models.Model):
    property = models.ForeignKey(Property , on_delete=CASCADE)
    photo = models.ImageField()"""

class Price(models.Model):
    date = models.DateTimeField()
    property = models.ForeignKey(Property , on_delete=CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.property.name + " price on "+ str(self.date)
    class Admin: 
        pass

#class Tenant(models.Model): 
    #person = models.OneToOneField(Person, on_delete=CASCADE)
    #property = models.ForeignKey(Property, on_delete = DO_NOTHING)