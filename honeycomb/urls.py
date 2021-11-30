from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('',dashboard, name = 'dashboard'),
    path('cashflow/',cashflow, name = 'cashflow'),
    path('payments/',payments, name = 'payments'),
    path('upload_data/',upload_data, name = 'upload_data'),
    re_path(r'^api/data/$', get_data, name = 'get_data' ),
    ]

