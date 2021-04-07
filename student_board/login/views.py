from student_board.register.models import Admin
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.apps import apps


# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        model_names = ["Admin", "Faculty", "Student"]
        user = authenticate(request, username=None, password=password, email=email)
        
        if user is not None:
            #login(request, user)
            request.session['user'] = user.id

            for model in model_names:
                Model = apps.get_model('register', model)
                if Model.object.filter(id=user.id).exists():
                    request.session['user_type'] = model
                    return HttpResponse('/')

            
        else:
            messages.info(request,'Email or password is incorrect')
    context={}
    return render(request, 'login/login.html', context)