import json
from time import time

import requests
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from payping.authentication import Bearer
from payping.payment import make_payment_code, get_url_payment, verify_payment
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from .models import *


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def goToPayment(request, code):
    return redirect(f'https://api.payping.ir/v2/pay/gotoipg/{code}')


def receivePayment(request):
    clientrefid = request.GET['clientrefid']
    refid = request.GET['refid']
    if refid is not 1:
        payment = Payment.objects.filter(refid=clientrefid).filter(done=False).last()

        header = Bearer(token=settings.PAYPING_TOKEN)
        url = 'https://api.payping.ir/v2/pay/verify'
        body = {
            "refId": refid,
            "amount": payment.subscription.price
        }
        res = requests.post(url, data=json.dumps(body), headers=header)

        if res.status_code is 200:
            payment.user.add_date_until(payment.subscription.days)
            payment.done = True
            payment.save()
            return render(request, 'pages/payment/payment_received.html', {
                'payment': payment, 'result': res.json(), 'refid': refid
            })
        else:
            return render(request, 'pages/payment/payment_received.html', {
                'payment': payment, 'result': res.json(), 'refid': refid
            })
