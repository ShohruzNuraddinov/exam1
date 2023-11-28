from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductView.as_view()),
    path('<int:pk>/', views.ProductGetView.as_view()),
    path('history/add/', views.HistoryAddView.as_view()),
    path('lesson/add/', views.LessonAddView.as_view())
]
