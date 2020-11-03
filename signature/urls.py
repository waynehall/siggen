from django.urls import path
from django.contrib import admin
from .views import create, index, SigView

urlpatterns = [
    path('',  index, name='index'),
    path('create/', create, name='create'),
    path('<int:pk>',  SigView, name='SigView'),
    path('?P<pk>[0-9]+)$', SigView, name='SigView'),
]