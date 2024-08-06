from django.urls import path
from ..views import Top10RatedBooksView,Top50SellingBooksView

urlpatterns = [
    path('top-10-rated-books/', Top10RatedBooksView.as_view(), name='top-10-rated-books'),
    path('top-50-selling-books/',Top50SellingBooksView.as_view(), name='top-50-selling-books')
]
