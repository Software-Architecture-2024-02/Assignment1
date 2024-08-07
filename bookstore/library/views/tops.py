from django.views.generic import ListView
from django.db.models import Avg,Sum
from library.models import Book, Sale


class Top10RatedBooksView(ListView):
    template_name = 'tops/top_rated_books.html'
    context_object_name = 'top_books_with_reviews'

    def get_queryset(self):
        # Get the top 10 rated books
        top_books = (
            Book.objects.annotate(avg_score=Avg('reviews__score'))
            .order_by('-avg_score')[:10]
        )

        top_books_with_reviews = []
        for book in top_books:
            highest_review = book.reviews.order_by('-score', '-number_of_upvotes').first()
            lowest_review = book.reviews.order_by('score', '-number_of_upvotes').first()
            top_books_with_reviews.append((book, highest_review, lowest_review))
        
        return top_books_with_reviews

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Top50SellingBooksView(ListView):
    template_name = 'tops/top_selling_books.html'
    context_object_name = 'top_selling_books_with_authors'

    def get_queryset(self):
        # Get the top 50 selling books
        top_selling_books = (
            Book.objects.annotate(total_sales=Sum('sales__sale'))
            .order_by('-total_sales')[:50]
        )

        top_selling_books_with_authors = []
        for book in top_selling_books:
            author_sales = Sale.objects.filter(book__author=book.author).aggregate(total_sales=Sum('sale'))['total_sales']
            was_top_5 = book.sales.filter(year=book.date_of_publication.year).order_by('-sale')[:5]
            top_selling_books_with_authors.append((book, author_sales, was_top_5.exists()))

        return top_selling_books_with_authors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
