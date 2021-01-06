from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ForumForm
from .models import forum,cevap
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
# Create your views here.

def liste(request):
    forumlar = forum.objects.all()
    context = {
        "forumlar" : forumlar
    }
    return render(request, "forum/liste.html", context)

def forumEkle(request):
    form = ForumForm(request.POST or None)

    if form.is_valid():
        forum = form.save(commit=False)
        forum.kullanici_id = request.user
        forum.save()
        messages.success(request,"forum başarıyla oluşturuldu")
        return redirect("index")
    return render (request, "forum/forumekle.html", {"form":form})

def detail(request, id):
    forumlar = forum.objects.filter(id = id).first()

    cevaplar = forumlar.cevaplar.all() 
    return render(request, "forum/detail.html", {"forumlar" : forumlar, "cevaplar" : cevaplar})

def yorumEkle(request, id):
    forumlar = get_object_or_404(forum, id = id)

    if request.method == "POST":
        cevap_kullanici = request.user
        mesaj = request.POST.get("yorum")

        yeniCevap = cevap(cevap_kullanici = cevap_kullanici, mesaj = mesaj)

        yeniCevap.forum = forumlar

        yeniCevap.save()
    return redirect("/forum/liste/forum/"+ str(id))