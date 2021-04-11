from django.db.models import Model
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.contrib import messages
from django.http import HttpResponse

from .forms import addAdminForm
from register.models import User, Admin, Student, Faculty

def userlist(request):
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

def approvals(request):
    context = {
        'students': Student.objects.filter(approved=False),
        'faculty' : Faculty.objects.filter(approved=False)
    }
    return render(request, 'admin/approvals.html', context)

def approve(request, user_id):
    for type in (Student, Faculty):
        try:
            user = type.objects.get(id=user_id)
            user.approved = True
            user.save()
            break
        except Model.DoesNotExist:
            pass
    return HttpResponseRedirect('/admin/approvals')

def deleteuser(requset, user_id):
    for type in (Student, Faculty):
        try:
            user = type.objects.get(id=user_id)
            user.delete()
            break
        except Model.DoesNotExist:
            pass
    return HttpResponseRedirect('/admin/userlist')
