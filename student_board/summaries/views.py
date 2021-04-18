from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Documents
from django.apps import apps
from django.core.files.storage import FileSystemStorage
from django.conf import settings


User = apps.get_model('register', 'User')

def addSum(request):
    return render(request, 'summaries/addSummary.html')

def submitSum(request):

    #add file to data folder
    newfile = request.FILES['file']
    fs = FileSystemStorage()
    fs.save(newfile.name, newfile)

    details = {
        'location'  : settings.MEDIA_ROOT,
        'title'     : newfile.name,
        'user'      : request.POST['id'],
        'course'    : request.POST['course'],
    }
    doc = Documents(**details)
    doc.save()
    
    return HttpResponseRedirect('/')