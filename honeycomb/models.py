from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.utils.translation import gettext_lazy as _ 

# Finish these before going home 
# 1. Make one graph using ajax in Jquery ( Sum of all properties of the owner)
# 2. 

# Create your models here.

#Why make Types inner class 
#1. It makes easy to understand the code. Here, we are using 



class User(AbstractUser): 
    class Types(models.TextChoices):
        LANDLORD = 'LANDLORD' , "Landlord"
        TENANT = 'TENANT' , "Tenant"
    type = models.CharField(_('Type'), max_length = 50 ,choices = Types.choices, default = Types.LANDLORD) # this itself is a field object
    name = models.CharField(_("Name of user"), blank = True, max_length = 255)
    
class LandlordManager(BaseUserManager): 
    def get_queryset(self, *args, **kwargs): 
        return super().get_queryset(*args, **kwargs).filter(type = User.Types.LANDLORD)

class Landlord(User):
    objects = LandlordManager()
    class Meta():
        proxy = True

    def save(self, *args, **kwargs): 
        # if the user doesn't exist
        if not self.pk:
            self.type = User.Types.LANDLORD 
        
        super().save(*args , **kwargs)


class TenantManager(BaseUserManager): 
    def get_queryset(self, *args, **kwargs): 
        return super().get_queryset(*args, **kwargs).filter(type = User.Types.TENANT)

class Tenant(User):
    objects = TenantManager()
    class Meta():
        proxy = True
    
    def save(self, *args, **kwargs): 
        # if user doesn't exist
        if not self.pk:
            self.type = User.Types.TENANT 
        
        super().save(*args , **kwargs)



"""class Person(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    email = models.EmailField()

    LANDLORD = 'LR'
    TENANT = 'T'
    
    USER_CHOICES = [
        (LANDLORD, 'Landlord'),
        (TENANT, 'Tenant'),
    ]
    user_types = models.CharField(
        max_length=2,
        choices=USER_CHOICES,
        default=LANDLORD,
    )

    class Admin:
        pass

    def __str__(self):
        return self.first_name + self.last_name

class Landlord(models.Model):
    person = models.OneToOneField(Person,on_delete=models.CASCADE,
        primary_key=True)
    
    class Admin: 
        pass

    def __str__(self):
        return self.person.first_name
"""

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