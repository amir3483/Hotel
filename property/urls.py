"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    
"""
from django.urls import path, include
from django.urls import re_path as url  # from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'property'

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('<int:id>', views.property_detail, name='property_detail'),
]
