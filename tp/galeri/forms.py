from django import forms
from .models import galeri

class GaleriForm(forms.ModelForm):
    class Meta:
        model = galeri
        fields = ["ad","yol","grup_id"]