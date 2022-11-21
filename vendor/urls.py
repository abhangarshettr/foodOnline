from django.urls import path,include
from . import views
from accounts import views as Accountviews

urlpatterns=[
    path('',Accountviews.vendorDashboard,name='vendor'),
    path('profile/',views.vprofile,name='vprofile'),
    path('menu-builder/',views.menu_builder,name='menu_builder'),
    path('menu-builder/category/<int:pk>/',views.fooditems_by_category,name='fooditems_by_category'),
    
   # cateogry CRUD
   path('menu-builder/category/add',views.add_category,name='add_category'),
   
    
]