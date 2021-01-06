from django.db import models
from datetime import datetime  
# Create your models here.

class forum(models.Model):
    baslik = models.CharField(max_length=99)
    icerik = models.TextField()
    kullanici_id = models.ForeignKey("auth.User", on_delete = models.CASCADE,default=0)
    grup_id = models.ForeignKey('grup.grup', on_delete = models.CASCADE, default=0)
    tarih = models.DateTimeField(default=datetime.now(),blank=True)
    def __str__(self):
        return self.baslik

class cevap(models.Model):
    forum = models.ForeignKey(forum, on_delete = models.CASCADE,verbose_name="cevap",related_name="cevaplar")
    cevap_kullanici = models.ForeignKey("auth.User", on_delete=models.CASCADE,default=0 )
    mesaj = models.TextField(verbose_name="mesaj")
    cevap_tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mesaj
