from quiz.models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from register.models import User
from django.utils import timezone
from django.urls import reverse

def index(request):
    context = {
        'questions' : Question.objects.all()
    }
    return render(request, 'quiz/quiz.html' , context)

def viewquestion(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/question.html', {'question': question})

def result(request, question_id):
    context = {
        'answer' : Choice.objects.get(pk=request.POST['choice'])
    }
    return render(request, 'quiz/result.html', context)

def add(request):
    return render(request, 'quiz/addquiz.html')

def submit_quiz(request):
    user = get_object_or_404(User, id=request.session['user'])
    date = timezone.now()
    quest = {
        'question_text' : request.POST['question_text'],
        'pub_date' : date,
        'poster' : user.last_name
    }
    question = Question(**quest)
    question.save()
    for i in range(1,5):
        text1 = 'choice_text'+str(i)
        correct = False
        check_correct = 'correct'+str(i)
        try:
            if (request.POST[check_correct]):
                correct = True
        except:
            pass
        choice = {
            'question' : question,
            'choice_text' : request.POST[text1],
            'correct' : correct
        }
        if (choice['choice_text'] != ''):
            choice1 = Choice(**choice)
            choice1.save()
    return HttpResponseRedirect(reverse('quiz:viewquestion', args=(question.id,)))
