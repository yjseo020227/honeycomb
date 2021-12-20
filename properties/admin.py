from django.contrib import admin

from .models import Property,Residential, Commerical,SingleResidentialUnit,SingleCommericalUnit

# Register your models here.
admin.site.register(Property)
admin.site.register(Residential)
admin.site.register(Commerical)
admin.site.register(SingleResidentialUnit)
admin.site.register(SingleCommericalUnit)