from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.apps import apps

Post = apps.get_model('posts', 'Post')
User = apps.get_model('register', 'User')

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/index.html', context)

def viewpost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post.html', context)

def addpost(request):
    return render(request, 'posts/addpost.html', {})

def sumbitpost(request):
    user = get_object_or_404(User, id=request.session['user'])
    forum = 'Genral'
    if (request.POST['forum_id'] != ''):
        forum = request.POST['forum_id']
    kw = {
        'poster'   : user.id,
        'title'    : request.POST['title'],
        'content'  : request.POST['content'],
        'date'     : timezone.now(),
        'forum_id' : forum # ALSO FIXME #good enough?
    }
    post = Post(**kw)
    post.save()
    return HttpResponseRedirect(reverse('posts:viewpost', args=(post.id,)))

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
    context = {
        'posts' : Post.objects.all().filter(forum_id='Jobs')
    }
    return render(request, 'posts/jobs.html', context)


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
    
#### end project funtions ####
