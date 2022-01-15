from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('home/', index, name='home'),

    path('musics/all/', allMusics, name='all_musics'),
    path('musics/create/', addMusic, name='add_music'),
    path('musics/<int:id>/', singleMusic, name='single_music'),
    path('musics/<int:id>/delete/', deleteMusic, name='delete_music'),

    path('categories/all/', allCategories, name='all_categories'),
    path('categories/create/', addCategory, name='add_category'),
    path('categories/<int:id>/', singleCategories, name='single_categories'),
    path('categories/<int:id>/delete/', deleteCategories, name='delete_categories'),

    path('users/all/', allUsers, name='all_users'),
    path('users/<int:id>/', singleUsers, name='single_users'),
    path('users/<int:id>/delete/', deleteUsers, name='delete_users'),

    path('timeofday/all/', allTime, name='all_times'),
    path('timeofday/create/', addTime, name='add_time'),
    path('timeofday/<int:id>/', singleTime, name='single_time'),
    path('timeofday/<int:id>/delete/', deleteTime, name='delete_time')
]
