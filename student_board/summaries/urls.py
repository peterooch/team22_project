from os import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'summaries'
urlpatterns = [
    path('', views.addSum, name='addSum'),
    path('submit', views.submitSum, name='submitSum'),
    path('facultySubmit', views.addSumFaculty, name='addSumFaculty'),
    path('view', views.viewSums, name='viewSums'),
    path('filterView', views.filterSums, name='filterSums'),
    path('delete/<str:title>/', views.deleteSum, name='deleteSum'),
] 
