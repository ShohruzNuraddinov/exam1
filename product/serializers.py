from rest_framework import serializers
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()


class UserSerailzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]


class LessonHistorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.LessonHistory
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    history = LessonHistorySerailizer(many=True)

    class Meta:
        model = models.Lesson
        fields = [
            'id',
            'title',
            'video',
            'duration',
            'history',
        ]


class ProductSubscribers(serializers.ModelSerializer):
    subscribers = UserSerailzier(many=True)

    class Meta:
        model = models.ProductSubscribers
        fields = [
            'product',
            'subscribers'
        ]


class ProductSerializer(serializers.ModelSerializer):
    videos = LessonSerializer(many=True)
    # subscribers = ProductSubscribers(many=True)

    class Meta:
        model = models.Product
        fields = [
            'author',
            'videos',
            'view_count',
            # 'subscribers',
        ]


class ProductAllSerializer(serializers.ModelSerializer):
    videos = LessonSerializer(many=True)
    subscribers = ProductSubscribers(many=True)

    class Meta:
        model = models.Product
        fields = [
            'author',
            'videos',
            'view_count',
            'subscribers',
        ]
