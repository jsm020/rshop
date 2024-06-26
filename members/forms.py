# forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    phone_number = forms.CharField(label='Telefon raqam', max_length=15, widget=forms.TextInput(attrs={'type': 'tel'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = self.fields['phone_number']
        self.fields['username'].widget.attrs.update({'type': 'tel'})
        del self.fields['phone_number']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            try:
                user = CustomUser.objects.get(phone_number=username)
            except CustomUser.DoesNotExist:
                raise forms.ValidationError("Foydalanuvchi topilmadi")

            if not user.check_password(password):
                raise forms.ValidationError("Noto'g'ri parol")

            self.user_cache = user
            return self.cleaned_data

        raise forms.ValidationError("Iltimos, telefon raqam va parolni kiriting")


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'type': 'text'}),
            'first_name': forms.TextInput(attrs={'type': 'text'}),
            'last_name': forms.TextInput(attrs={'type': 'text'}),
            'email': forms.EmailInput(attrs={'type': 'email'}),
            'phone_number': forms.TextInput(attrs={'type': 'tel'}),
            'password1': forms.PasswordInput(attrs={'type': 'password'}),
            'password2': forms.PasswordInput(attrs={'type': 'password'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email avval ro'yxatdan o'tgan")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu username avval ro'yxatdan o'tgan")
        return username

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Bu nomer avval ro'yxatdan o'tgan")
        return phone_number



class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number')
        widgets = {
            'first_name': forms.TextInput(attrs={'type': 'text'}),
            'last_name': forms.TextInput(attrs={'type': 'text'}),
            'email': forms.EmailInput(attrs={'type': 'email'}),
            'phone_number': forms.TextInput(attrs={'type': 'tel'}),
        }
