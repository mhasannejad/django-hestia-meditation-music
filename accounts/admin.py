from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Music)
admin.site.register(Subscription)
admin.site.register(Verification)
admin.site.register(TimeOfDay)
admin.site.register(Favorite)
admin.site.register(Article)