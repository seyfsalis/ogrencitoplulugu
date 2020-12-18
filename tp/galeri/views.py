from django.shortcuts import render

# Create your views here.

def listele(request):
    return render(request, 'galeri/liste.html')