from django.urls import path
from . import views

app_name="quiz"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.viewquestion, name='viewquestion'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('add', views.add, name='add'),
    path('submit/', views.submit_quiz, name='submit_quiz')
]