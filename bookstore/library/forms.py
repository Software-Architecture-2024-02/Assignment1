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
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].label_from_instance = lambda obj: obj.name
    class Meta:
        model = Book
        fields = ['name', 'summary', 'date_of_publication', 'number_of_sales', 'author']
        widgets = {
            'date_of_publication': forms.DateInput(attrs={'type': 'date'}),
        }

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['book'].label_from_instance = lambda obj: obj.name
    class Meta:
        model = Review
        fields = ['book', 'review', 'score', 'number_of_upvotes']
        widgets = {
            'score': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields['book'].label_from_instance = lambda obj: obj.name
    class Meta:
        model = Sale
        fields = ['book', 'year', 'sale']
        widgets = {
            'year': forms.NumberInput(attrs={'min': 1000, 'max': 2024}),
        }
