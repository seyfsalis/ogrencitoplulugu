from django.shortcuts import render,HttpResponse

# Create your views here.

def liste(request):
    return render(request, "forum/liste.html")