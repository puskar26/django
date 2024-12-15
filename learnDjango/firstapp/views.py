from django.shortcuts import render
from django.http import HttpResponse
from .models import SuperHeroes

# Create your views here.

def firstapp_home(request):
    heroes = SuperHeroes.objects.all()
    return render(request, 'firstapp/index.html',{'heroes':heroes})

def login(response):
    return HttpResponse("This is login page.")