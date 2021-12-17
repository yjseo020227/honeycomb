from django.urls import path, re_path, include
from .views import *

  

urlpatterns = [
    path('', dashboard, name = 'dashboard'),
    path('cashflow/',cashflow, name = 'cashflow'),
    path('payments/',payments, name = 'payments'),
    path('upload_data/',upload_data, name = 'upload_data'),


    re_path(r'^api/data/$', get_data, name = 'get_data' ),
    ]


    #path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/signup/', chooseSignUp, name='signup'),
    #path('accounts/signup/student/', landlordSignUp, name='landlord_signup'),
    #path('accounts/signup/teacher/', tenantSignUp, name='tenant_signup'),
    
    
    
    

