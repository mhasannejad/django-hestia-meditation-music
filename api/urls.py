from django.contrib import admin
from django.urls import path
from .auth_views import *
from .views import *

urlpatterns = [
    path('auth/sms/request/', sendVerificationSMS),
    path('auth/sms/verify/', verifyMySMS),

    path('home/', homeContent),

    path('profile/edit/', updateProfile),
    path('profile/details/', profileDetails),

    path('pay/build/', buildPayment),

    path('category/all/', allCategories),
    path('category/time/<int:time>/', getTimeCategory),
    path('category/<int:category>/', getCategory),

    path('category/musics/<int:category>/', musicsByCategory),
    path('music/<int:music>/', getMusic),

    path('fav/music/<int:music>/', addMusicToFavorites),
    path('fav/mine/', myFavorites),

    path('subscriptions/all/', allSubscriptions),

    path('article/all/', allArticles),

]
