from django.urls import path

from . import views

app_name = 'admin'
urlpatterns = [
    path('userlist', views.userlist, name='userlist'),
    path('addAdmin', views.addAdmin, name='addAdmin'),
    path('approvals', views.approvals, name='approvals'),
    path('approve/<user_id>/', views.approve, name='approve'),
    path('deleteuser/<user_id>/', views.deleteuser, name='deleteuser'),
    path('convert/<user_id>/', views.student_to_faculty, name='convert'),
    path('convert', views.student_to_faculty),
]