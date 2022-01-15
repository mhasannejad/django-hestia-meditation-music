from random import randint

import factory
from factory.django import DjangoModelFactory
from .models import *


class UserGenerator(DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Faker("first_name")
    email = factory.Faker('email')


class MusicGenerator(DjangoModelFactory):
    class Meta:
        model = Music

    title = factory.Faker('file_name')
    file = 'musics/yt1s.com_-_NEFFEX_Want_Me_5lg90w4.mp3'
    cover = 'covers/music/cover.png'

    category = Category.objects.all()[randint(1, len(Category.objects.all()) - 1)]
