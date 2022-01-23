from django.contrib import admin

from .models import Property,SingleRentalUnit

# Register your models here.
admin.site.register(Property)
admin.site.register(SingleRentalUnit)