from django.shortcuts import render
from django.template import loader

def index(request):
    context = {
        'test': "yolo lastico"
    }
    return render(request, 'index.html', context)