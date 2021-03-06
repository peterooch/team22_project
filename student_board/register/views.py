from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render

from .models import Student,Faculty
# ...
def index(request):
    return render(request, 'register.html')

def adduser(request):
    # FIXME add validation
    kw = {
        'first_name' : request.POST['firstname'],
        'last_name'  : request.POST['lastname'],
        'id'         : request.POST['ID'],
        'email'      : request.POST['email'],
        'department' : request.POST['department'],
        'password'   : request.POST['psw']
    }
    student = Student(**kw)
    student.save()
    request.session['user'] = student.id
    request.session['user_type'] = 'Student'
    return HttpResponseRedirect('/')

def facultyReg(request):
    return render(request, 'FacultyRegister.html')

def facultyRegister(request):
    details = {
        'first_name' : request.POST['firstname'],
        'last_name'  : request.POST['lastname'],
        'id'         : request.POST['ID'],
        'email'      : request.POST['email'],
        'password'   : request.POST['psw'],
        'courses'    : request.POST['courses']
    }
    faculty = Faculty(**details)
    faculty.save()
    request.session['user'] = faculty.id
    request.session['user_type'] = 'Faculty'
    return HttpResponseRedirect('/')
