from django.urls import path, include
from .views import *
from .import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views



urlpatterns = [

    path('admin/', admin.site.urls),
    path('home', ReactView.as_view()),
    path('index', views.index, name='index'),
    path('1', views.ram_ram),
    path('city',  views.Search_Route, name='Search_Route'),
    path('signup',  views.sign_up, name='sign_up'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('delete', views.delete, name='delete'),
    path('cab', views.cab, name='cab'),


]
