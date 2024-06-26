# admin.py
from django.contrib import admin
from .models import SliderRasm,CategoryRasm,LogoRasmlar
from django.utils.safestring import mark_safe

@admin.register(SliderRasm)
class SliderRasmAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_display')
    readonly_fields = ('img_display',)

    def img_display(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="200" height="auto" />')

    img_display.short_description = 'Image Preview'
@admin.register(CategoryRasm)
class CategoryRasmAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_display')
    readonly_fields = ('img_display',)

    def img_display(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="200" height="auto" />')

    img_display.short_description = 'Image Preview'
class LogoRasmlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_link_display')

admin.site.register(LogoRasmlar, LogoRasmlarAdmin)