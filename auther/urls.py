from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('login/', loginF, name='login'),
    path('register/', registerF, name='register'),
    path('logout/', logoutF, name='logout'),

]
