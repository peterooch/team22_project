from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from register.models import Admin, User

def Home(request):
    if Admin.objects.all().exists() is False:
        return HttpResponseRedirect(reverse('admin:addAdmin'))

    logged = False
    user_type = None
    friendly = ''
    if 'user_type' in request.session:
        user_type = request.session['user_type']
        logged = True
        user = User.objects.get(id=request.session['user'])
        friendly = f'{user.first_name} {user.last_name}'

    context = { 
        'logged'    : logged,
        'user'      : user_type,
        'user_friendly': friendly,
        }
    return render(request, 'Home.html', context)

def Logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('Home:Home'))

