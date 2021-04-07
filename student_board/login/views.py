from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.apps import apps



from register.models import User, Student, Faculty, Admin
# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=None, password=password, email=email)
        
        if user is not None:
            #login(request, user)
            request.session['user'] = user.id

            # check if the user is a student
            StudentModel = apps.get_model('register', 'Student')
            if StudentModel.objects.filter(id=user.id).exists():
                return HttpResponse("student logged in") #FIXME: redirect to student homepage

            #FIXME: check if the user is faculty or admin
        else:
            messages.info(request,'Email or password is incorrect')
    context={}
    return render(request, 'login/login.html', context)