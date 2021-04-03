from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render

from .models import Student
# ...
def index(request):
    return render(request, 'register.html')

def adduser(request):
    # FIXME add validation
    kw = {
        'first_name' : request.POST['firstname'],
        'last_name'  : request.POST['lastname'],
        'Id'         : request.POST['ID'],
        'email'      : request.POST['email'],
        'department' : request.POST['department'],
        'password'   : request.POST['psw']
    }
    student = Student(**kw)
    student.save()
    return HttpResponseRedirect('/')
