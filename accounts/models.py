from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
from django.db import models
from django.db.models.deletion import CASCADE,SET_NULL
from django.db.models.fields import DateField
from django.utils.translation import gettext_lazy as _


# Create your models here.

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
    related_commerical_properties = models.ForeignKey('properties.SingleCommericalUnit' , null = True , on_delete = SET_NULL)
    related_residential_properties = models.ForeignKey('properties.SingleResidentialUnit' , null = True , on_delete = SET_NULL)
    
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
