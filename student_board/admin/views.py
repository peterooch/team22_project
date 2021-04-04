from django.shortcuts import render

from django.http.response import HttpResponse, HttpResponseRedirect


# ...
def index(request):
    return render(request, 'admin/userlist.html')
