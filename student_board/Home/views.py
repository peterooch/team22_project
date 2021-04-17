from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

def Home(request):
    return render(request, 'Home.html')

