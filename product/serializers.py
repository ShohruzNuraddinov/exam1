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
        fields = [
            'id',
            'user',
            'product',
            'lesson',
            'end_point',
            'status',
            'created_at',
            'updated_at',
        ]


class LessonHistoryMainSerailizer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='title'
    )

    class Meta:
        model = models.LessonHistory
        fields = [
            'id',
            'user',
            'product',
            'lesson',
            'end_point',
            'status',
            'created_at',
            'updated_at',
        ]


class LessonMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = [
            'id',
            'title',
            'video',
            'duration',
            'created_at',
            'updated_at',
        ]


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
            'created_at',
            'updated_at',
        ]


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False, slug_field='username', read_only=True
    )
    videos = serializers.SlugRelatedField(
        many=True, slug_field='title', read_only=True
    )
    # subscribers = ProductSubscribers(many=True)

    class Meta:
        model = models.Product
        fields = [
            'id',
            'author',
            'title',
            'videos',
            'view_count',
            # 'subscribers',
            'created_at',
            'updated_at',
        ]


class ProductAllSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False, slug_field='username', read_only=True
    )
    videos = LessonMainSerializer(many=True)
    # subscribers = ProductSubscribers(many=True)

    class Meta:
        model = models.Product
        fields = [
            'id',
            'author',
            'videos',
            'view_count',
            'subscribers',
            'update_view_count',
            'created_at',
            'updated_at',
        ]


class ProductSubscribers(serializers.ModelSerializer):
    # subscribers = UserSerailzier(many=False)
    product = serializers.SlugRelatedField(
        many=False, slug_field='title', read_only=True)

    class Meta:
        model = models.ProductSubscribers
        fields = [
            'product',
            # 'subscribers'
        ]


class UserLessonSerializer(serializers.ModelSerializer):
    products = ProductSubscribers(many=True)
    user_history = LessonHistoryMainSerailizer(many=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'products',
            'user_history', 
        ]
