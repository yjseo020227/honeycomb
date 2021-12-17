from django.urls import path, re_path, include
from .views import *

  

urlpatterns = [
    path("", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout", logout_request, name= "logout"),
    path('honeycomb',include('honeycomb.urls')),
    re_path(r'^api/data/$', get_data, name = 'get_data' ),
    ]
