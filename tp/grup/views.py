from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def liste(request):
    return render(request, "grup/list.html")