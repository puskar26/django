from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def firstapp_home(request):
    return render(request, 'firstapp/index.html')

def login(response):
    return HttpResponse("This is login page.")