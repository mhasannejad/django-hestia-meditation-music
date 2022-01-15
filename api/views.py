from django.conf import settings
from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
from accounts.models import *
from payments.models import Payment
from .serializers import *


# Create your views here.


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def homeContent(request):
    right_now = int(datetime.now().hour)
    selected_time = 3
    if right_now <= 10:
        selected_time = settings.MORNING
    elif 10 < right_now < 17:
        selected_time = settings.NOON
    else:
        selected_time = settings.NIGHT

    time_of_day = TimeOfDay.objects.get(key=selected_time)
    category = Category.objects.filter(time_of_day=time_of_day).order_by('?')
    musics = Music.objects.filter(category__in=category)[:3]

    articles = Article.objects.all()
    return Response({
        'musics': MusicSerializerListItem(
            musics, many=True
        ).data,
        'articles': ArticleSerializer(
            articles, many=True
        ).data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def allCategories(request):
    all_categories = Category.objects.all()
    all_daytimes = TimeOfDay.objects.all()
    return Response(
        {
            'categories': CategorySerializerListItem(
                all_categories, many=True
            ).data,
            'daytimes': TimeOfDaySerializer(
                all_daytimes, many=True
            ).data
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getTimeCategory(request, time):
    time_of_Day = TimeOfDay.objects.get(id=time)
    all_categories = time_of_Day.category_set.all()
    return Response(

        CategorySerializerListItem(
            all_categories, many=True
        ).data,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getCategory(request, category):
    all_categories = Category.objects.get(id=category)

    return Response(
        CategorySerializerDetailed(
            all_categories, many=False
        ).data,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getMusic(request, music):
    music = Music.objects.get(id=music)

    return Response(
        MusicSerializerDetailed(
            music, many=False
        ).data,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def musicsByCategory(request, category):
    category = Category.objects.get(id=category)

    return Response(
        MusicSerializerListItem(
            category.music_set, many=True
        ).data,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def allSubscriptions(request):
    all_categories = Subscription.objects.all()

    return Response(
        SubscriptionSerializer(
            all_categories, many=True
        ).data,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def addMusicToFavorites(request, music):
    music = Music.objects.get(id=music)
    user = User.objects.get(id=request.user.id)
    if len(Favorite.objects.filter(user=user).filter(music=music)) > 0:
        fav = Favorite.objects.filter(user=user).filter(music=music).first()
        fav.delete()
        return Response(
            status=status.HTTP_200_OK
        )
    else:
        Favorite.objects.create(
            user=user,
            music=music
        )
        return Response(
            status=status.HTTP_201_CREATED
        )


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def buildPayment(request):
    payment_code = request.POST['payment_code']
    refid = request.POST['refid']
    user = User.objects.get(id=request.user.id)
    subscription = Subscription.objects.get(id=request.POST['subscription_id'])
    Payment.objects.create(
        user=user, subscription=subscription, time=time(), code=payment_code, refid=refid
    )
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def myFavorites(request):
    my_fav = Music.objects.filter(favorite__user=request.user).order_by('-id')
    print(request.user.id)
    return Response(
        MusicSerializerListItem(
            my_fav, many=True
        ).data,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def allArticles(request):
    articles = Article.objects.all()

    return Response(
        ArticleSerializer(
            articles, many=True
        ).data,
        status=status.HTTP_200_OK
    )
