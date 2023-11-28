from rest_framework import serializers

from . import models


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
            # 'video_duration',
            'history',
        ]


class ProductSerializer(serializers.ModelSerializer):
    videos = LessonSerializer(many=True)
    # history = LessonHistorySerailizer(many=False)

    class Meta:
        model = models.Product
        fields = [
            'author',
            'videos',
            'view_count',
            # 'history',
        ]
