from django.contrib import admin
from .models import User,Landlord,Tenant
# Register your models here.
admin.site.register(User)
admin.site.register(Landlord)
admin.site.register(Tenant)