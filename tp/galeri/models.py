from django.db import models
from grup.models import Grup
# Create your models here.

class galeri(models.Model):
    yol = models.FileField(blank=True, null=True)
    kullanici_id = models.ForeignKey("auth.User", on_delete = models.CASCADE,default=0)
    grup_id = models.ForeignKey('grup.grup', on_delete = models.CASCADE, default=0)

    def __str__(self):
        return self.yol