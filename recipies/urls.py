
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.get_routes, name='Routes'),
     path('recipies', views.get_recipies, name='Recipies'),
     path('recipe/<str:pk>', views.get_recipe, name='Recipe'),
]
