from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to My webpage. I am Pushkar Niraula.")
    return render(request,'index.html')

def about(request):
    return HttpResponse("This is the about section.")

def projects(request):
    return HttpResponse("This is the projects section.")