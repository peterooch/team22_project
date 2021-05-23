from quiz.models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

def index(request):
    context = {
        'questions' : Question.objects.all()
    }
    return render(request, 'quiz/quiz.html' , context)

def viewquestion(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/question.html', {'question': question})

def result(request, answer_id):
    answer = get_object_or_404(Choice, pk=answer_id)
    return render(request, 'quiz/result.html', {'answer':answer})
