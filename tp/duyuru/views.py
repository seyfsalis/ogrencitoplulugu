from django.shortcuts import render,HttpResponse
from .models import Duyuru
# Create your views here.

def index(request):
    return render(request, 'index.html')

def listele(request):
    return render(request, "duyuru/liste.html")