from django.shortcuts import render
from django.apps import apps
from .forms import addAdminForm
from register.models import Admin
from django.contrib import messages
from django.http import HttpResponse

def userlist(request):
    User = apps.get_model('register', 'User')
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admin/userlist.html', context)


def addAdmin(request):
    form=addAdminForm()
    if request.method == 'POST':
        form=addAdminForm(request.POST)
        if form.is_valid():
            args= {
                'email' : request.POST['email'],
                'password'  : request.POST['password'],
                'first_name'  : request.POST['first_name'],
                'last_name'  : request.POST['last_name'],
                'id'  : request.POST['id']
            }
            new_admin=Admin(**args)
            #add try and except for entering the same id
            new_admin.save()
            return HttpResponse('added new admin') #FIX TO REDIRECT
        else:
            messages.info(request,'form not valid')

    context={'form': form}
    return render(request, 'admin/addAdmin.html', context)