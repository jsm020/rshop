from django.contrib import admin
from .models import Mahsulot, mahsulotRasmlari,Kategoriya,mahsulotReyting,ReviewProducts

class mahsulotRasmlariInline(admin.TabularInline):
    model = mahsulotRasmlari
    extra = 1  # Nechta qo'shimcha bo'sh forma bo'lishini belgilaydi
    fields = ('rasmi',)  # Ko'rsatiladigan maydonlar

class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi', 'tavsif', 'kategoriya')  # Ro'yxatda ko'rsatiladigan ustunlar
    inlines = [mahsulotRasmlariInline]

admin.site.register(Mahsulot, MahsulotAdmin)
admin.site.register(Kategoriya)
admin.site.register(mahsulotReyting)
admin.site.register(ReviewProducts)
