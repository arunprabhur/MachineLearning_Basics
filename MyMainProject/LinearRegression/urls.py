from django.contrib import admin
from django.urls import path
from LinearRegression import views

urlpatterns = [
    path('', views.hello, name='LR View'),
]
