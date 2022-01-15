from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .decorators import *

# Create your views here.
from .forms import RegisterForm


@unauthenticated_user
def loginF(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password is incorrect', )
            return render(request, 'pages/auth/login.html')

    else:
        return render(request, 'pages/auth/login.html')


@unauthenticated_user
def registerF(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'pages/auth/register.html', {'form': form})


def logoutF(request):
    logout(request)
    return redirect('login')
