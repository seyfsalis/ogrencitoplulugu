from django.contrib import admin
from .models import galeri
# Register your models here.

@admin.register(galeri)
class GaleriAdmin(admin.ModelAdmin):

    list_display = ["ad"]
    list_display_links = ["ad"]
    search_fields = ["ad"]
    class Meta:
        model = galeri