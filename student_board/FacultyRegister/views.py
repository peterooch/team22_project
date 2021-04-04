from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

from .models import Faculty

def FacultyRegister(request):
    context= {}
    #return render(request,'FacultyRegister/FacultyRegister', context)
    return HttpResponse('Faculty Register')