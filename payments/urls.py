from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('topay/<str:code>/', goToPayment),
    path('receive/', receivePayment),

]
