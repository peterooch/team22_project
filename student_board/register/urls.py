from os import name
from django.urls import path

from . import views

app_name = 'register'
urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.adduser, name='submit'),
    path('facultyReg', views.facultyReg, name='facultyReg'),
    path('facultyRegister', views.facultyRegister, name='submit2'),
]