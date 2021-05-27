from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.apps import apps
from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_aware, make_aware
from admin.models import Rules

def get_aware_datetime(date_str):
    ret = parse_datetime(date_str)
    if not is_aware(ret):
        ret = make_aware(ret)
    return ret

Post = apps.get_model('posts', 'Post')
User = apps.get_model('register', 'User')

forum_ids = ['General', 'milga', 'Jobs', 'Social', 'project', 'study', 'apartment', 'private teaching']
forum_ids.sort()

def index(request):
    posts = list(Post.objects.all())
    for post in posts:
        try:
            post.poster_user = User.objects.get(id=post.poster)
        except:
            post.poster_user = post.poster
    
    context = {
        'posts': posts,
        'user_type': request.session['user_type'],
    }
    return render(request, 'posts/index.html', context)

def viewpost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post.html', context)

def deletepost(request, post_id):
    if request.session['user_type'] == 'Admin':
        post = get_object_or_404(Post, id=post_id)
        post.delete()
    return HttpResponseRedirect(reverse('posts:index'))

def addpost(request):
    return render(request, 'posts/addpost.html', {'forum_ids': forum_ids})

def sumbitpost(request):
    user = get_object_or_404(User, id=request.session['user'])
    forum = 'General'
    if (request.POST['forum_id'] != ''):
        forum = request.POST['forum_id']
    if 'zoomdate' in request.POST:
        date = request.POST['zoomdate']
        date = get_aware_datetime(date)

    else:
        date = timezone.now()

    kw = {
        'poster'   : user.first_name,
        'title'    : request.POST['title'],
        'content'  : request.POST['content'],
        'date'     : date,
        'forum_id' : forum # ALSO FIXME #good enough?
    }
    post = Post(**kw)
    post.save()

    return HttpResponseRedirect(reverse('posts:index'))

##### scholarship functions ####

def searchmilga(request):
    context = {
        'posts' : Post.objects.all().filter(forum_id='milga')
    }
    return render(request, 'posts/scholarship.html', context)

def milgabydate(request):
    context = {
        'posts' : Post.objects.all().filter(forum_id='milga').filter(date__gte=request.POST['fday'])
    }
    return render(request, 'posts/scholarship.html', context)

def milgabyword(request):
    context = {
        'posts' : Post.objects.all().filter(forum_id='milga').filter(content__contains=request.POST['kword'])
    }
    return render(request, 'posts/scholarship.html', context)
    

#### job searching functions ####

def searchJobs(request):
    if Rules.objects.filter(forum='Jobs').first() is None:
        rules = None
    else:
        rules = Rules.objects.filter(forum='Jobs').first().rules
    if request.method == 'POST':
        word = request.POST['search']
        date = request.POST['date']
        context = {
            'posts' : Post.objects.all().filter(forum_id='Jobs' , title__contains=word, content__contains=word, date__contains=date ),
            'date'  : timezone.now(),
            'rules' : rules
        }
    else:
        context = {
            'posts' : Post.objects.all().filter(forum_id='Jobs'),
            'date'  : timezone.now(),
            'rules' : rules
        }
    return render(request, 'posts/jobs.html', context)

def searchSocial(request):
    if Rules.objects.filter(forum='Social').first() is None:
        rules = None
    else:
        rules = Rules.objects.filter(forum='Social').first().rules
    if request.method == 'POST':
        word = request.POST['search']
        date = request.POST['date']
        context = {
            'posts' : Post.objects.all().filter(forum_id='Social' , title__contains=word, content__contains=word, date__contains=date ),
            'date'     : timezone.now(),
            'rules' : rules
        }
    else:
        context = {
            'posts' : Post.objects.all().filter(forum_id='Social'),
            'date'     : timezone.now(),
            'rules' : rules
        }
    return render(request, 'posts/social.html', context)


##### project functions ####

def searchproject(request):
    # filter for project forum
    context = {
        'posts' : Post.objects.all().filter(forum_id='project')
    }

    return render(request, 'posts/projects.html', context)

def projectbydate(request):
    #filter withing project forum to start from specific date
    context = {
        'posts' : Post.objects.all().filter(forum_id='project').filter(date__gte=request.POST['fday'])
    }

    return render(request, 'posts/projects.html', context)

def projectbyword(request):
    #search withing project content with a keyword
    context = {
        'posts' : Post.objects.all().filter(forum_id='project').filter(content__contains=request.POST['kword'])
    }

    return render(request, 'posts/projects.html', context)
    
#### study-partners funtions ####

def studybuddy(request):

    context = {
        'posts' : Post.objects.all().filter(forum_id='study')
    }

    return render(request, 'posts/study.html', context)

def zoomlink(request):
    return render(request, 'posts/zoom.html')


def studydate(request):
    
    context = {
        'posts' : Post.objects.all().filter(forum_id='study').filter(date__gte=request.POST['fday'])
    }

    return render(request, 'posts/study.html', context)

def studyword(request):
    
    context = {
        'posts' : Post.objects.all().filter(forum_id='study').filter(content__contains=request.POST['kword'])
    }

    return render(request, 'posts/study.html', context)

##### apartment forum functions ####

def searchapartment(request):
    # filter for apartment forum
    context = {
        'posts' : Post.objects.all().filter(forum_id='apartment')
    }

    return render(request, 'posts/apartment.html', context)

def apartmentbydate(request):
    #filter withing apartment forum to start from specific date
    context = {
        'posts' : Post.objects.all().filter(forum_id='apartment').filter(date__gte=request.POST['fday'])
    }

    return render(request, 'posts/apartment.html', context)

def apartment_key_word(request):
    #search withing apartment forum with a keyword
    context = {
        'posts' : Post.objects.all().filter(forum_id='apartment').filter(content__contains=request.POST['kword'])
    }

    return render(request, 'posts/apartment.html', context)

##### private teaching forum functions ####

def searchateacher(request):
    context = {
        'posts' : Post.objects.all().filter(forum_id='private teaching')
    }
    return render(request, 'posts/privateteaching.html', context)

def teachingbydate(request):
    #filter an private teacher post from specific date
    context = {
        'posts' : Post.objects.all().filter(forum_id='private teaching').filter(date__gte=request.POST['fday'])
    }

    return render(request, 'posts/privateteaching.html', context)

def teaching_keyword(request):
    #search withing private teaching forum with a keyword
    context = {
        'posts' : Post.objects.all().filter(forum_id='private teaching').filter(content__contains=request.POST['kword'])
    }
    return render(request, 'posts/privateteaching.html', context)


