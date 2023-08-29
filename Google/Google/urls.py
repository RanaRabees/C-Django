"""Google URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views
admin.site.site_header  =  " !!! Administrator_page !!! "  
admin.site.site_title   =  "!!! Administrator_page !!!"
admin.site.index_title  =  "!!! Admin_portal !!!"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('index/',views.index,name='index'),
    path('base/',views.base,name='base'), 
    path('chrome/',include('chrome.urls')),
    path('facebook/',include('facebook.urls')), 
    path('instagram/',include('instagram.urls')),
    path('yahoo/',include('yahoo.urls')),
    path('twitter/',include('twitter.urls')),  
    path('book/',views.book,name='book'),
    path('text/',views.text,name='text'),
    path('harry/',views.harry,name='harry'),
        
]
