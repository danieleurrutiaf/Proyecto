from django.shortcuts import render

# Create your views here.


def index(request): 
    context = {}
    return render(request, 'taller1/index.html', context) 