from os import name
from django.urls import path

from . import views

app_name = 'register'
urlpatterns = [
    path('', views.index),
    path('submit', views.adduser, name='submit'),
]