from os import name
from django.urls import path

from . import views

app_name = 'summaries'
urlpatterns = [
    path('', views.addSum, name='addSum'),
    path('submit', views.submitSum, name='submitSum'),
]