from django.shortcuts import render

# Create your views here.

def all_items(request):
    return render(request, 'firstProject/all_files.html')