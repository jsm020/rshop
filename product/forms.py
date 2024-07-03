# forms.py
from django import forms
from .models import ReviewProducts
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['manzil', 'viloyat', 'shahar', 'pochta_kodi', 'telefon_raqam']
        labels = {
            'manzil': 'Manzil',
            'viloyat': 'Viloyat',
            'shahar': 'Shahar',
            'pochta_kodi': 'Pochta kodi',
            'telefon_raqam': 'Telefon raqam',
        }
        widgets = {
            'manzil': forms.TextInput(attrs={'type': 'text'}),
            'viloyat': forms.TextInput(attrs={'type': 'text'}),
            'shahar': forms.TextInput(attrs={'type': 'text'}),
            'pochta_kodi': forms.TextInput(attrs={'type': 'text'}),
            'telefon_raqam': forms.TextInput(attrs={'type': 'tel'}),
        }
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewProducts
        fields = ['izoh', 'reyting']
        widgets = {
            'izoh': forms.Textarea(attrs={'placeholder': 'Izoh qoldirish'}),
            'reyting': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }



class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Izlash...'})
    )