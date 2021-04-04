<<<<<<< Updated upstream
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

from .models import Faculty

def FacultyRegister(request):
    context= {}
    #return render(request,'FacultyRegister/FacultyRegister', context)
    return HttpResponse('Faculty Register')
=======
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Faculty

def index(request):
    return render(request, 'register.html')

def adduser(request):
    details = {
        'first_name' : request.POST['firstname'],
        'last_name'  : request.POST['lastname'],
        'Id'         : request.POST['ID'],
        'email'      : request.POST['email'],
        'password'   : request.POST['psw'],
        'courses'    : request.POST['courses']
    }
    faculty = Faculty(**details)
    faculty.save()
    return HttpResponseRedirect('/')
>>>>>>> Stashed changes
