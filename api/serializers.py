from easy_thumbnails.templatetags.thumbnail import thumbnail_url
from rest_framework import serializers

from accounts.models import *


class ThumbnailSerializer(serializers.ImageField):
    def __init__(self, alias, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_only = True
        self.alias = alias

    def to_representation(self, value):
        if not value:
            return None

        url = thumbnail_url(value, self.alias)
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url


class UserSelfProfileSerializer(serializers.ModelSerializer):
    avatar = ThumbnailSerializer(alias='avatar')

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'token', 'avatar', 'payed_until', 'payed_until_now', 'phone']


class CategorySerializerListItem(serializers.ModelSerializer):
    cover = ThumbnailSerializer(alias='small')

    class Meta:
        model = Category
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class MusicSerializerDetailed(serializers.ModelSerializer):
    category = CategorySerializerListItem(many=False)

    class Meta:
        model = Music
        fields = ['id', 'title', 'description', 'category', 'file', 'cover']


class MusicSerializerListItem(serializers.ModelSerializer):
    cover_thumbnail = ThumbnailSerializer(alias='small', source='cover')

    class Meta:
        model = Music
        fields = '__all__'


class CategorySerializerDetailed(serializers.ModelSerializer):
    musics = MusicSerializerListItem(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'cover', 'musics']


class ArticleSerializer(serializers.ModelSerializer):
    cover_thumbnail = ThumbnailSerializer(alias='small', source='cover')

    class Meta:
        model = Article
        fields = ['id', 'title', 'caption', 'cover', 'time', 'cover_thumbnail']


class TimeOfDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeOfDay
        fields = '__all__'
