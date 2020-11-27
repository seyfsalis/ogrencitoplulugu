from django.db import models
from grup.models import Grup
# Create your models here.

class Duyuru(models.Model):
    baslik = models.CharField(max_length=150, verbose_name='başlık')
    icerik = models.TextField(verbose_name='duyuru içeriği')
    tarih = models.DateTimeField(auto_now_add=True)
    kullanici_id = models.ForeignKey("auth.User", on_delete = models.CASCADE,default=0)
    grup_id = models.ForeignKey('grup.grup', on_delete = models.CASCADE, default=0)


    def __str__(self):
        return self.baslik