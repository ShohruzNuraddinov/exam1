from rest_framework import generics
from django.contrib.auth import get_user_model
from django.db.models import Sum, F, Count, Avg
from django.db.models.functions import Coalesce

from rest_framework.response import Response

from . import models
from . import serializers

User = get_user_model()

# Create your views here.


class ProductView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductGetView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductAllSerializer

    # def get(self, request, pk):
    #     serializer = self.get_serializer(
    #         models.Product.objects.filter(
    #             Q(subscribers__subscribers=request.user)).get(id=pk)
    #     )
    #     # serializer.is_valid(raise_exception=True)
    #     # data = serializer.validated_data
    #     # print(data)
    #     return Response(serializer.data)


class LessonAddView(generics.CreateAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonMainSerializer


class LessonHistoryView(generics.CreateAPIView):
    queryset = models.LessonHistory.objects.all()
    serializer_class = serializers.LessonHistorySerailizer


class UserLessonsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserLessonSerializer


class MainStatistic(generics.GenericAPIView):
    def get(self, request):
        queryset = models.Product.objects.aggregate(
            main_view_count=Sum('view_count'),
            time_spent=Sum('product_history__end_point'),
            hits_lesson=Count('product_history'),
            product_sale_percent=Count(
                'view_count') / Count("subscribers__subscribers") * 100,
        )

        return Response(queryset)
