from django.urls import path

from . import views

app_name = 'admin'
urlpatterns = [
    path('userlist', views.userlist, name='userlist')
]