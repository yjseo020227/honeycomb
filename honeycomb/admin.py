from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Landlord)
admin.site.register(Tenant)
admin.site.register(Property)
admin.site.register(Price)