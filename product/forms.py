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



class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Izlash...'})
    )