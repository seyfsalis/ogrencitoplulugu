from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import etkinlik
# Create your views here.

def liste(request):
    etkinlikler = etkinlik.objects.all()
    context = {
        "etkinlikler" :etkinlikler
    }
    return render(request, "etkinlik/liste.html", context)

def detail(request, id):
    #etkinlikler = etkinlik.objects.filter(id = id).first()
    etkinlikler = get_object_or_404(etkinlik, id = id)
    return render(request, "etkinlik/detail.html", {"etkinlikler": etkinlikler})