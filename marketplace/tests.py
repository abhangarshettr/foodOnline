from django.test import TestCase
from django.urls import path
from . import views
# Create your tests here.

urlpatterns = [
    path('',views.marketplace,name='marketplace'),
    
]