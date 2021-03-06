from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.contrib import messages
from django.http import HttpResponse

from summaries.models import Documents
from .forms import addAdminForm
from register.models import User, Admin, Student, Faculty
from django.contrib import messages
from .models import Rules, AdminAlert
from django.urls import reverse

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
            try:
                new_admin.save()
            except:
                messages.info(request,'Email already in use')
                context={}
                return render(request, 'admin/addAdmin.html', context)
            return HttpResponseRedirect('/')
        else:
            messages.info(request,'form not valid')
    first_run = Admin.objects.all().exists() is False  
    context={'form': form, 'first_run': first_run}
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
        except ObjectDoesNotExist:
            pass
    return HttpResponseRedirect('/admin/approvals')

def deleteuser(requset, user_id):
    for type in (Student, Faculty):
        try:
            user = type.objects.get(id=user_id)
            user.delete()
            break
        except ObjectDoesNotExist:
            pass
    return HttpResponseRedirect('/admin/userlist')

def student_to_faculty(request, user_id = None):
    ctx = { 'students': Student.objects.all() }

    if user_id is None:
        return render(request, 'admin/student_to_faculty.html', ctx)

    student = None
    try:
        student = Student.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return render(request, 'admin/student_to_faculty.html', ctx)

    kw = {
        'id': student.id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'email': student.email,
        'password': student.password,
        'approved': student.approved,
        'courses': ''
    }
    student.delete()
    faculty = Faculty(**kw)
    faculty.save()
    return render(request, 'admin/student_to_faculty.html', ctx)


def addRules(request):
    context = {
        'forums' : {'milga', 'Jobs', 'Social', 'project', 'study', 'apartment', 'private teaching'}
    }
    return render(request, 'admin/rules.html', context)

def submitRules(request):
    # if there are no rules to the forum, add. otherwise overrun
    
    forum = request.POST['forum']
    if Rules.objects.filter(forum=forum).first() is None:
        details = {
           'forum' :   forum,
           'rules' :   request.POST['rules']
        }
        new_rules = Rules(**details)
        new_rules.save()
        messages.info(request,'Rules added!')
    
    else:
        rules = Rules.objects.get(forum=forum)
        rules.rules = request.POST['rules']
        rules.save()
        messages.info(request,'Rules updated!')

    return HttpResponseRedirect(reverse('admin:addRules'))

def alerts(request):
    context = {
        'alerts': AdminAlert.objects.all(),
    }
    return render(request, 'admin/alerts.html', context)

def deletealert(request, alert_id):
    alert = AdminAlert.objects.get(id=alert_id)
    alert.delete()
    return HttpResponseRedirect(reverse('admin:alerts'))

def handlealert(request, alert_id):
    alert = AdminAlert.objects.get(id=alert_id)
    try:
        alert.document.delete()
        alert.delete()
    except:
        pass
    return HttpResponseRedirect(reverse('admin:alerts'))

def newalert(request, doc_id):
    return render(request, 'admin/newalert.html', { 'doc_id': doc_id })

def createalert(request):
    kw = {
        'reporter' : User.objects.get(id=request.session['user']),
        'document' : Documents.objects.get(id=request.POST['doc_id']),
        'info'     : request.POST['info'],
    }
    alert = AdminAlert(**kw)
    alert.save()
    return HttpResponseRedirect(reverse('summaries:viewSums'))