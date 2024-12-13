from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello . This is home page.")
     return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello . This is about page.")

def projects(request):
    return HttpResponse("Hello . This is projects page.")
