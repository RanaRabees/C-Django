
from django.urls import path
from . import views



urlpatterns = [

    path('',views.home,name='twitter/home.html'),
    
    
    
]