from django.db import models
from accounts.models import Subscription, User


# Create your models here.

class Payment(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=15,null=True)
    time = models.IntegerField(null=True)
    done = models.BooleanField(default=False)
    refid = models.CharField(max_length=255,null=True)
