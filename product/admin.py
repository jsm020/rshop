from django.contrib import admin
from .models import Mahsulot, mahsulotRasmlari,Kategoriya,ReviewProducts,Cart, CartItem

class mahsulotRasmlariInline(admin.TabularInline):
    model = mahsulotRasmlari
    extra = 1  # Nechta qo'shimcha bo'sh forma bo'lishini belgilaydi
    fields = ('rasmi',)  # Ko'rsatiladigan maydonlar

class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi', 'tavsif', 'kategoriya')  # Ro'yxatda ko'rsatiladigan ustunlar
    inlines = [mahsulotRasmlariInline]

admin.site.register(Mahsulot, MahsulotAdmin)
admin.site.register(Kategoriya)
# admin.site.register(mahsulotReyting)
admin.site.register(ReviewProducts)
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    inlines = [CartItemInline]

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)