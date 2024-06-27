# forms.py
from django import forms
from .models import ReviewProducts

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewProducts
        fields = ['izoh', 'reyting']
        widgets = {
            'izoh': forms.Textarea(attrs={'placeholder': 'Izoh qoldirish'}),
            'reyting': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
