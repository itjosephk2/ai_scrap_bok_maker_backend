from django.contrib import admin
from .models import ScrapImage


@admin.register(ScrapImage)
class ScrapImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'aesthetic', 'caption', 'created_at']
    readonly_fields = ['caption', 'edited_image']
