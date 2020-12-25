from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Duyuru
# Create your views here.

def index(request):
    return render(request, 'index.html')

def listele(request):
    duyurular = Duyuru.objects.all()
    context = {
        "duyurular" :duyurular
    }
    return render(request, "duyuru/liste.html", context)

def detail(request, id):
    #duyuru = Duyuru.objects.filter(id = id).first()
    duyuru = get_object_or_404(Duyuru, id = id)
    return render(request, "duyuru/detail.html", {"duyuru": duyuru})