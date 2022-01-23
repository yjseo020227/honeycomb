from django.forms import ModelForm
from .models import Property, SingleRentalUnit

class PropertyForm(ModelForm):
    class Meta: 
        model = Property
        #fields = '__all__'
        fields = ['name', 'address', 'photos', 'property_type' , 'number_of_floors', 'number_of_rentals']

    """def save(self, user, commit = True):
        property = super(PropertyForm,self).save(commit = False)
        property.landlord = user

        if commit: 
            property.save()
        return property"""

class SingleUnitForm(ModelForm): 
    class Meta: 
        model = SingleRentalUnit
        fields = ['tenant', 'monthly_rental','floor', 'business_type']