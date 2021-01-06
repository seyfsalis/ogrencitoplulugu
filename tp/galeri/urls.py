from django.urls import path
from . import views

urlpatterns = [
    path('liste/', views.listele, name='galeri-liste'),
    path("galeriekle/", views.fotografEkle, name="galeri-ekle"),
]