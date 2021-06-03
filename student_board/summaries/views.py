from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Documents, Feedback
from django.urls import reverse
from register.models import User
from django.apps import apps
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from collections import namedtuple

def addSum(request, additional = False):
    context = { 'additional': additional}
    return render(request, 'summaries/addSummary.html', context)

def addMat(request):
    return addSum(request, additional=True)

def submitSum(request):

    #add file to data folder
    newfile = request.FILES['file']
    fs = FileSystemStorage()
    fs.save(newfile.name, newfile)
    file_size = fs.size(newfile.name)

    details = {
        'location'  : settings.MEDIA_ROOT,
        'title'     : newfile.name,
        'user'      : request.session['user'],
        'course'    : request.POST['course'],
        'file_size' : file_size,
        'additional': (request.POST['additional'] == 'True')
    }
    doc = Documents(**details)
    doc.save()
    
    return HttpResponseRedirect('view')

def viewFeedback(request, id):

    context = {
        'document'  : Documents.objects.get(id=id),
        'feedbacks' : Feedback.objects.filter(DocumentID__id=id)
    }
    return render(request, 'summaries/viewfeedback.html', context)

def addfeedback(request):

    context = {
        'feedback' :  request.POST['feedback'],
        'DocumentID' : Documents.objects.get(id=request.POST['id'])
    }
    FB = Feedback(**context)
    FB.save()
    return HttpResponseRedirect(reverse('summaries:viewSums'))

def feedback(request, id):
    context = {
        'id' : id
    }
    return render(request, 'summaries/feedBack.html', context)

Pair = namedtuple('Pair', ['bool_val', 'title'])
doc_pairs = [Pair(False, 'Summaries'), Pair(True, 'Additional Materials')]

def viewSums(request):
    
    if 'user_type' in request.session:
        user_type = request.session['user_type']
    else:
        user_type = None

    context = {
        'user_type': user_type,
        'users': User.objects.all(),
        'courses': Documents.objects.values_list('course', flat=True).distinct(),
        'docs': Documents.objects.all(),
        'pairs': doc_pairs,
    }
    return render(request, 'summaries/viewSums.html', context)

def filterSums(request):
    c=request.POST['course']
    if (c=='all'):
        context = {
            'users': User.objects.all(),
            'courses': Documents.objects.values_list('course', flat=True).distinct(),
            'docs': Documents.objects.all(),
            'pairs': doc_pairs,
        }
    else:
        context = {
            'users': User.objects.all(),
            'courses': Documents.objects.values_list('course', flat=True).distinct(),
            'docs': Documents.objects.all().filter(course=c),
            'pairs': doc_pairs,
        }
    return render(request, 'summaries/viewSums.html', context)


def deleteSum(request, title):
    sum = get_object_or_404(Documents, title=title)
    sum.delete()
    return HttpResponseRedirect(reverse('summaries:viewSums'))