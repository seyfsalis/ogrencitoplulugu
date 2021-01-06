from django.db import models
from grup.models import Grup
from datetime import datetime
# Create your models here.

class galeri(models.Model):
    ad = models.CharField(max_length=50,verbose_name="ad")
    yol = models.FileField(blank=True, null=True,verbose_name="Fotoğraf ekleyin")
    kullanici_id = models.ForeignKey("auth.User", on_delete = models.CASCADE,default=0)
    grup_id = models.ForeignKey('grup.Grup', on_delete = models.CASCADE, default=0)
    tarih = models.DateTimeField(default=datetime.now(),blank=True)
    def __str__(self):
        return self.ad