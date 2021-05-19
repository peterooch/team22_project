from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.deletepost, name='deletepost'),
    path('<int:post_id>/', views.viewpost, name='viewpost'),
    path('add', views.addpost, name='addpost'),
    path('submit', views.sumbitpost, name='submitpost'),
    path('scholarship',views.searchmilga, name='searchmilga'),
    path('jobs',views.searchJobs, name='searchJobs'),
    path('scholarshipdate',views.milgabydate, name='milgabydate'),
    path('scholarshipword',views.milgabyword, name='milgabyword'),
    path('project',views.searchproject, name='searchproject'),
    path('projectdate',views.projectbydate, name='projectbydate'),
    path('projectword',views.projectbyword, name='projectbyword'),
    path('study',views.studybuddy, name='studybuddy'),
    path('studydate',views.studydate, name='studydate'),
    path('studyword',views.studyword, name='studyword'),
    path('apartment',views.searchapartment, name='searchapartment'),
    path('apartmentbydate',views.apartmentbydate, name='apartmentbydate'),
    path('apartment_key_word',views.apartment_key_word, name='apartment_key_word'),
    path('zoom', views.zoomlink, name='zoomlink'),
    path('social', views.searchSocial, name='searchSocial'),
    path('social', views.searchSocial, name='searchSocial'),
    path('privateteaching',views.searchateacher, name='searchateacher'),
    path('teachingbydate',views.teachingbydate, name='teachingbydate'),
    path('teaching_keyword',views.teaching_keyword, name='teaching_keyword')
]