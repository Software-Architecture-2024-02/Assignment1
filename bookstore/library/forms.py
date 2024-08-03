from django import forms
from .models import Author, Book, Review, Sale

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth', 'country_of_origin', 'short_description']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'summary', 'date_of_publication', 'number_of_sales']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'review', 'score', 'number_of_upvotes']
        widgets = {
            'score': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['book', 'year', 'sale']
        widgets = {
            'year': forms.NumberInput(attrs={'min': 2000, 'max': 2100}),
        }
