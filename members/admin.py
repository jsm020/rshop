# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'phone_number')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')

    def get_form(self, request, obj=None, **kwargs):
        print("CustomUserAdmin get_form called")
        return super().get_form(request, obj, **kwargs)

admin.site.register(CustomUser, CustomUserAdmin)
