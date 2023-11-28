from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers

# Create your views here.


class ProductView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductGetView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductAllSerializer


class HistoryAddView(generics.CreateAPIView):
    queryset = models.LessonHistory.objects.all()
    serializer_class = serializers.LessonHistorySerailizer


class LessonAddView(generics.CreateAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
