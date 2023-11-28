from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.ProductView.as_view()),
    path('product/<int:pk>/', views.ProductGetView.as_view()),

    path('lesson/add/', views.LessonAddView.as_view()),
    path('lesson/history/add/', views.LessonHistoryView.as_view()),

    path('user/<int:pk>/product/', views.UserLessonsView.as_view()),

    path('statistic/main/', views.MainStatistic.as_view()),
    # path('statistic/lesson/timespent-count/', views.TimeStentCount.as_view()),
    # path('statistic/lesson/history-count/', views.LessonHistoryCount.as_view())
]
