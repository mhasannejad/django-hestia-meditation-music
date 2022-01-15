from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    return render(request, 'pages/interface/main.html')


def test(request):
    return render(request,'pages/payment/payment_received.html')
