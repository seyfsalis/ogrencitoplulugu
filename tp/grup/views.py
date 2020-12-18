from django.shortcuts import render

# Create your views here.


def liste(request):
    return render(request, "grup/list.html")