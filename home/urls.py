from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("learn",views.learn,name='learn'),
    path("contact",views.contact,name='contact')

    
]
