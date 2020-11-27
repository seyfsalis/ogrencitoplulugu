from django.contrib import admin
from .models import etkinlik
# Register your models here.

@admin.register(etkinlik)
class EtkinlikAdmin(admin.ModelAdmin):

    list_display = ["baslik"]
    list_display_links = ["baslik"]
    search_fields = ["baslik"]
    class Meta:
        model = etkinlik