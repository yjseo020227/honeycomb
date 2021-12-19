from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Landlord

from django.contrib.auth import get_user_model
User = get_user_model()
#Create your forms here

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","type", "password1", "password2", )
    
    def save(self, commit=True):
        user = super(NewUserForm,self).save(commit = False)
        user.email = self.cleaned_data['email']
        #user.type = "TENANT"
        
        if commit:
            user.save()
        return user