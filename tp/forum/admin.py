from django.contrib import admin
from .models import forum,cevap
# Register your models here.

admin.site.register(cevap)

@admin.register(forum)
class ForumAdmin(admin.ModelAdmin):

    list_display = ["baslik"]
    list_display_links = ["baslik"]
    search_fields = ["baslik"]
    class Meta:
        model = forum