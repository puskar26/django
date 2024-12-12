from django.http import HttpResponse

def home(response):
    return HttpResponse("Hello . This is home page.")

def about(response):
    return HttpResponse("Hello . This is about page.")

def projects(response):
    return HttpResponse("Hello . This is projects page.")
