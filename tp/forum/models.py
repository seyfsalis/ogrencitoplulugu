from django.db import models

# Create your models here.

class forum(models.Model):
    baslik = models.CharField(max_length=99)
    icerik = models.TextField()
    kullanici_id = models.ForeignKey("auth.User", on_delete = models.CASCADE,default=0)
    grup_id = models.ForeignKey('grup.grup', on_delete = models.CASCADE, default=0)

    def __str__(self):
        return self.baslik