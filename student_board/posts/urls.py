from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.viewpost, name='viewpost'),
    path('add', views.addpost, name='addpost'),
    path('submit', views.sumbitpost, name='submitpost'),
    path('scholarship',views.searchmilga, name='searchmilga'),
    path('jobs',views.searchJobs, name='searchJobs'),
    path('scholarshipdate',views.milgabydate, name='milgabydate'),
    path('scholarshipword',views.milgabyword, name='milgabyword')
]