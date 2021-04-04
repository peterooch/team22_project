from django.shortcuts import render
from django.apps import apps

def userlist(request):
    User = apps.get_model('register', 'User')
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admin/userlist.html', context)
