from django.contrib import admin
from .models import Duyuru
# Register your models here.

@admin.register(Duyuru)
class DuyuruAdmin(admin.ModelAdmin):

    list_display = ["baslik", "tarih"]
    list_display_links = ["baslik", "tarih"]
    search_fields = ["baslik"]
    list_filter = ["tarih"]
    class Meta:
        model = Duyuru