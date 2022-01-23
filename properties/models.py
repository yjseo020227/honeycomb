from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _ 

# Create your models here.
class Property(models.Model):
    class PropertyType(models.TextChoices):
        OFFICETEL = 'O', _('Officetel')
        APARTMENT = 'A', _('Apartment')
        COMMERCIAL = 'C', _('Commerical')
    
    landlord = models.ForeignKey('accounts.Landlord',on_delete=models.CASCADE , null = True)
    name = models.CharField(max_length= 100)
    address = models.CharField(max_length = 500)
    photos = models.ImageField(null = True , blank = True)
    property_type = models.CharField(max_length = 1, choices = PropertyType.choices , default = PropertyType.APARTMENT)
    number_of_floors = models.IntegerField()
    number_of_rentals = models.IntegerField()
    
    
    

    def __str__(self):
        return self.address

    def get_owner(self):
        return self.landlord.person.first_name
    
    
    def setPrice(self , price):
        self.recent_price = price

    class Admin:
        pass
class SingleRentalUnit(models.Model):
    property = models.ForeignKey('Property', on_delete= models.CASCADE)
    tenant = models.ForeignKey('accounts.Tenant', on_delete=models.CASCADE, null =True, blank = True)
    monthly_rental = models.FloatField(null = True, blank = True)
    floor = models.IntegerField()
    business_type = models.CharField(max_length = 30)

    def __str__(self):
        landlord_username = self.property.landlord.username
        property_name = self.property.name
        floor = self.floor 
        property_list = SingleRentalUnit.objects.filter(property__landlord__username = landlord_username, floor = floor)

        count = 0 
        for single_rental_unit in property_list.iterator():
            if single_rental_unit.id == self.id:
                return property_name + " "+ str(floor)+" floor" + "(" + str(count) + ")"
            else: 
                count+=1


        #returns the list of properties if the properties match up with the landlord
        #you need return all single rental uniuts within the same floor as the currect one and find its id within that queryset 
        

    def return_valid_ending(self):
        pass

