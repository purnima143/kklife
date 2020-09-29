from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'kklife/index.html')

def blogs(request):
    return render(request, 'kklife/blogs.html')

def joinnow(request):
    if request.method == 'POST':
        return render( request, 'kklife/joinnow.html' )
    return render(request, 'kklife/joinnow.html')

def team(request):
    return render(request, 'kklife/team.html')
