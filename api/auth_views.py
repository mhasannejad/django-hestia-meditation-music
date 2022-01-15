import json
import random
import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import *
import time
from melipayamak import Api
from .serializers import *


@api_view(['POST'])
def sendVerificationSMS(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    verifications_sent_to_this_number = Verification.objects.filter(ip=ip)
    current_time = time()
    if Verification.objects.filter(ip=ip).count() > 0:
        if abs(Verification.objects.filter(ip=ip).last().time - current_time) < 1:
            return Response(status=status.HTTP_409_CONFLICT)

    code = random.randint(100000, 999999)
    current_time = time()
    phone = request.POST['phone_number']
    print(phone)


    """
    
    implement the fucking code sms sender here
    
    
    """

    username = '09385242988'
    password = 'AE0NQ'
    api = Api(username, password)
    sms_soap = api.sms('soap')
    to = phone
    resutl = sms_soap.send_by_base_number([code], to, 68288)
    if User.objects.filter(phone=phone).exists():
        user = User.objects.get(phone=phone)
    else:
        user = User.objects.create(
            phone=phone
        )
    verification = Verification.objects.create(
        code=code,
        time=current_time,
        user=user,
        ip=ip
    )
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def verifyMySMS(request):
    code = request.POST['verification_code']
    phone_number = request.POST['phone_number']
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    verifications_sent_to_this_number = Verification.objects.filter(user__phone=phone_number)
    print(time())
    if verifications_sent_to_this_number.last().code == code:
        if abs(verifications_sent_to_this_number.filter(code=code).last().time - time()) > 60 * 60:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            user = User.objects.get(phone=phone_number)
            user.phone_verified = True
            user.save()
            this_numbers_verifications = Verification.objects.filter(user=user)
            this_numbers_verifications.update(used=True)
        return Response(UserSelfProfileSerializer(user, many=False).data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = User.objects.get(id=request.user.id)
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.save()
    return Response(UserSelfProfileSerializer(user, many=False).data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profileDetails(request):
    user = User.objects.get(id=request.user.id)
    return Response(UserSelfProfileSerializer(user, many=False).data, status=status.HTTP_200_OK)
