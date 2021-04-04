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
    user = get_object_or_404(User, Id=request.session['user'])
    kw = {
        'poster'   : user.Id,
        'title'    : request.POST['title'],
        'content'  : request.POST['content'],
        'date'     : timezone.now(),
        'forum_id' : 'General', # ALSO FIXME
    }
    post = Post(**kw)
    post.save()
    return HttpResponseRedirect(reverse('posts:viewpost', args=(post.id,)))
