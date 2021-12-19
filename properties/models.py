from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _ 

# Create your models here.
class Property(models.Model):
    class PropertyType(models.TextChoices):
        RESIDENTIAL = 'R', _('Residential')
        COMMERCIAL = 'C', _('Commerical')
    
    class Meta: 
        abstract = True
    landlord = models.ForeignKey('accounts.Landlord',on_delete=models.CASCADE , null = True)
    address = models.CharField(max_length = 500)
    name = models.CharField(max_length = 500)
    photos = models.ImageField()
    property_type = models.CharField(max_length = 1, choices = PropertyType.choices , default = PropertyType.RESIDENTIAL )
    
    

    def __str__(self):
        return self.name

    def get_owner(self):
        return self.landlord.person.first_name
    
    
    def setPrice(self , price):
        self.recent_price = price

    class Admin:
        pass

class Residential(Property):
    number_of_rentals = models.IntegerField()

class SingleResidentialUnit(models.Model):
    residential_property = models.ForeignKey(Residential, on_delete = CASCADE)
    monthly_rental = models.FloatField()

class Commerical(Property):
    floors = models.IntegerField()
    underground = models.BooleanField()

class SingleCommericalUnit(models.Model):
    commerical_property = models.ForeignKey(Commerical, on_delete = CASCADE)
    floor = models.IntegerField()
    business_type = models.CharField(max_length = 30)
    monthly_rental = models.FloatField()
