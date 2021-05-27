from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

def Home(request):
    logged = False
    if 'user_type' in request.session:
        user_type = request.session['user_type']
        logged = True
    context = { 
        'logged' : logged,
        }
    return render(request, 'Home.html', context)

def Logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('Home:Home'))

