from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Documents
from register.models import User
from django.apps import apps
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def addSum(request):
    return render(request, 'summaries/addSummary.html')

def submitSum(request):

    #add file to data folder
    newfile = request.FILES['file']
    fs = FileSystemStorage()
    fs.save(newfile.name, newfile)
    file_size = fs.size(newfile.name)

    details = {
        'location'  : settings.MEDIA_ROOT,
        'title'     : newfile.name,
        'user'      : request.POST['id'],
        'course'    : request.POST['course'],
        'file_size' : file_size,
    }
    doc = Documents(**details)
    doc.save()
    
    return HttpResponseRedirect('view')


def viewSums(request):
    context = {
        'users': User.objects.all(),
        'courses': Documents.objects.values_list('course', flat=True).distinct(),
        'docs': Documents.objects.all(),
    }
    return render(request, 'summaries/viewSums.html', context)

def filterSums(request):
    c=request.POST['course']
    if (c=='all'):
        context = {
            'users': User.objects.all(),
            'courses': Documents.objects.values_list('course', flat=True).distinct(),
            'docs': Documents.objects.all()
        }
    else:
        context = {
            'users': User.objects.all(),
            'courses': Documents.objects.values_list('course', flat=True).distinct(),
            'docs': Documents.objects.all().filter(course=c)
        }
    return render(request, 'summaries/viewSums.html', context)