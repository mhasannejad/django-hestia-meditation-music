from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from accounts.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from auther.decorators import admin_only
from panel.forms import *


@login_required(login_url='login')
@admin_only
def index(request):
    print(request.user.id)
    return render(request, 'pages/panel/index.html')


@login_required(login_url='login')
@admin_only
def allMusics(request):
    musics = Paginator(Music.objects.order_by('-id'), 50)
    page = request.GET.get('page', 1)
    if request.method == 'POST':
        musics = Paginator(Music.objects.filter(title__contains=request.POST.get('statements')).order_by('-id'), 50)
    try:
        cs = musics.page(page)
    except PageNotAnInteger:
        cs = musics.page(1)
    except EmptyPage:
        cs = musics.page(musics.num_pages)

    return render(request, 'pages/panel/music/all.html', {'musics': cs})


@login_required(login_url='login')
@admin_only
def singleMusic(request, id):
    music = Music.objects.get(id=id)
    music_form = MusicForm(instance=music)
    if request.method == 'POST':
        music_form = MusicForm(instance=music, data=request.POST)
        if music_form.is_valid():
            music_form.save()
            return render(request, 'pages/panel/music/single.html', {'music': music, 'music_form': music_form})
        else:
            return HttpResponse(status=500)
    return render(request, 'pages/panel/music/single.html', {'music': music, 'music_form': music_form})


@login_required(login_url='login')
@admin_only
def deleteMusic(request, id):
    music = Music.objects.get(id=id)
    music.delete()
    return redirect('all_musics')


@login_required(login_url='login')
@admin_only
def allCategories(request):
    categories = Paginator(Category.objects.order_by('-id'), 50)
    page = request.GET.get('page', 1)
    if request.method == 'POST':
        categories = Paginator(Category.objects.filter(title__contains=request.POST.get('statements')).order_by('-id'),
                               50)
    try:
        cs = categories.page(page)
    except PageNotAnInteger:
        cs = categories.page(1)
    except EmptyPage:
        cs = categories.page(categories.num_pages)

    return render(request, 'pages/panel/category/all.html', {'categories': cs})


@admin_only
def singleCategories(request, id):
    category = Category.objects.get(id=id)
    category_form = CategoryForm(instance=category)
    if request.method == 'POST':
        category_form = CategoryForm(instance=category, data=request.POST)
        if category_form.is_valid():
            category_form.save()
            return render(request, 'pages/panel/category/single.html',
                          {'category': category, 'category_form': category_form})
        else:
            return HttpResponse(status=500)
    return render(request, 'pages/panel/category/single.html', {'category': category, 'category_form': category_form})


@login_required(login_url='login')
@admin_only
@admin_only
@admin_only
def deleteCategories(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('all_categories')


@login_required(login_url='login')
@admin_only
def allUsers(request):
    users = Paginator(User.objects.order_by('-id'), 50)
    page = request.GET.get('page', 1)
    if request.method == 'POST':
        users = Paginator(User.objects.filter(title__contains=request.POST.get('statements')).order_by('-id'), 50)
    try:
        cs = users.page(page)
    except PageNotAnInteger:
        cs = users.page(1)
    except EmptyPage:
        cs = users.page(users.num_pages)

    return render(request, 'pages/panel/user/all.html', {'users': cs})


@login_required(login_url='login')
@admin_only
def singleUsers(request, id):
    user = User.objects.get(id=id)
    user_form = UserForm(instance=user)
    if request.method == 'POST':
        user_form = UserForm(instance=user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, 'pages/panel/user/single.html',
                          {'user': user, 'user_form': user_form})
        else:
            return HttpResponse(status=500)
    return render(request, 'pages/panel/user/single.html', {'user': user, 'user_form': user_form})


@login_required(login_url='login')
@admin_only
def deleteUsers(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('all_users')


@login_required(login_url='login')
@admin_only
def allTime(request):
    timeofdays = Paginator(TimeOfDay.objects.order_by('-id'), 50)
    page = request.GET.get('page', 1)
    if request.method == 'POST':
        timeofdays = Paginator(TimeOfDay.objects.filter(title__contains=request.POST.get('statements')).order_by('-id'),
                               50)
    try:
        cs = timeofdays.page(page)
    except PageNotAnInteger:
        cs = timeofdays.page(1)
    except EmptyPage:
        cs = timeofdays.page(timeofdays.num_pages)

    return render(request, 'pages/panel/timeofday/all.html', {'timeofdays': cs})


@login_required(login_url='login')
@admin_only
def singleTime(request, id):
    timeofday = TimeOfDay.objects.get(id=id)
    timeofday_form = TimeOfDayForm(instance=timeofday)
    if request.method == 'POST':
        timeofday_form = TimeOfDayForm(instance=timeofday, data=request.POST)
        if timeofday_form.is_valid():
            timeofday_form.save()
            return render(request, 'pages/panel/timeofday/single.html',
                          {'timeofday': timeofday, 'timeofday_form': timeofday_form})
        else:
            return HttpResponse(status=500)
    return render(request, 'pages/panel/timeofday/single.html',
                  {'timeofday': timeofday, 'timeofday_form': timeofday_form})


@login_required(login_url='login')
@admin_only
def deleteTime(request, id):
    timeofday = TimeOfDay.objects.get(id=id)
    timeofday.delete()
    return redirect('all_timeofdays')


@login_required(login_url='login')
@admin_only
def addTime(request):
    timeofday_form = TimeOfDayForm()
    if request.method == 'POST':
        timeofday_form = TimeOfDayForm(request.POST)
        if timeofday_form.is_valid():
            timeofday_form.save()
            return render(request, 'pages/panel/timeofday/create.html',
                          {'timeofday_form': timeofday_form})
        else:
            return HttpResponse(timeofday_form.errors)
    return render(request, 'pages/panel/timeofday/create.html',
                  {'timeofday_form': timeofday_form})


@login_required(login_url='login')
@admin_only
def addCategory(request):
    category_form = CategoryForm()
    if request.method == 'POST':
        category_form = CategoryForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return render(request, 'pages/panel/category/create.html',
                          {'category_form': category_form})
        else:
            return HttpResponse(category_form.errors)
    return render(request, 'pages/panel/category/create.html',
                  {'category_form': category_form})


@login_required(login_url='login')
@admin_only
def addMusic(request):
    music_form = MusicForm()
    if request.method == 'POST':
        music_form = MusicForm(request.POST, request.FILES)
        if music_form.is_valid():
            music_form.save()
            return render(request, 'pages/panel/music/create.html',
                          {'music_form': music_form})
        else:
            return HttpResponse(music_form.errors)
    return render(request, 'pages/panel/music/create.html',
                  {'music_form': music_form})
