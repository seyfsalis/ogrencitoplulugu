from django.contrib import admin
from .models import galeri
# Register your models here.

@admin.register(galeri)
class GaleriAdmin(admin.ModelAdmin):

    list_display = ["yol"]
    list_display_links = ["yol"]
    search_fields = ["yol"]
    class Meta:
        model = galeri