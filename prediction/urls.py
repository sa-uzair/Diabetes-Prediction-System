from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'prediction'
urlpatterns = [

    path('', views.Home,name="Home"),
    path('form/', views.prediction , name="prediction"),
    path('form/result', views.result , name="result")

]
