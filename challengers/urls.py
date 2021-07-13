from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='challengers-index'),
    path('default/', views.auto_create_challenger_test_result, name='challengers-default'),
    path('default-result/', views.auto_create_result_single, name='challengers-default-result'),
    path('sevice/', views.service, name='challengers-service'),
]
