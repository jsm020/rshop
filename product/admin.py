from django.contrib import admin
from django.urls import reverse
from .models import Checkout, Mahsulot, mahsulotRasmlari,Kategoriya,ReviewProducts,Cart, CartItem,Wishlist
from django.utils.html import format_html

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
    list_display = ('cart', 'product', 'quantity','total_price',)

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi')

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    filter_horizontal = ('products',)

admin.site.register(Wishlist, WishlistAdmin)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'cart_link', 'narxi','manzil', 'viloyat', 'shahar', 'pochta_kodi', 'telefon_raqam', 'created_at']
    list_filter = ['created_at']
    search_fields = ['manzil', 'viloyat', 'shahar', 'pochta_kodi', 'telefon_raqam']
    date_hierarchy = 'created_at'

    def cart_link(self, obj):
        cart_id = obj.cart.id
        url = reverse('admin:product_cart_change', args=[cart_id])
        return format_html('<a href="{}">{}</a>', url, cart_id)

    cart_link.short_description = 'Cart'

admin.site.register(Checkout, CheckoutAdmin)