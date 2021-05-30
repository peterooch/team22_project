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
    path('rules', views.addRules, name='addRules'),
    path('submitRules', views.submitRules, name='submitRules'),
    path('alerts', views.alerts, name='alerts'),
    path('deletealert/<alert_id>/', views.deletealert, name='deletealert'),
    path('handlealert/<alert_id>/', views.handlealert, name='handlealert'),
    path('newalert/<doc_id>/', views.newalert, name='newalert'),
    path('createalert', views.createalert, name='createalert'),
]