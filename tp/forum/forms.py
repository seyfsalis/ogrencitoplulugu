from django import forms
from .models import forum
class ForumForm(forms.ModelForm):
    class Meta:
        model = forum
        fields = ["baslik", "icerik", "grup_id"]