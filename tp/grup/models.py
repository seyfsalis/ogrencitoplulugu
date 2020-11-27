from django.db import models

# Create your models here.
class Grup(models.Model):
    ad = models.CharField(max_length=99)

    def __str__(self):
        return self.ad