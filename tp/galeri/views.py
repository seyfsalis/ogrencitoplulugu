from django.shortcuts import render,redirect
from .forms import GaleriForm
from django.contrib import messages
from .models import galeri
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.

def listele(request):
    galeriler = galeri.objects.all()
    context = {
        "galeriler" : galeriler
    }
    return render(request, "galeri/liste.html", context)

def fotografEkle(request):
    form = GaleriForm(request.POST or None,request.FILES or None)
    print(request.FILES)
    if form.is_valid():
        galeriler = form.save(commit=False)
        galeriler.kullanici_id = request.user
        galeriler.save()
        messages.success(request,"fotoğraf başarıyla yüklendi")
        return render (request, "galeri/galeriekle.html", context={"galeriler":galeriler})
    #return render (request, "galeri/galeriekle.html", context={"galeriler":galeriler})
    return render (request, "galeri/galeriekle.html", {"form":form})

    def __str__(self):
        return self.ad