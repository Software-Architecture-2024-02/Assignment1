from django.shortcuts import render
from django.db.models import Avg, Max, Min, Sum
from library.models import Book, Review, Sale, Author

def Home(request):
    # Obtener los 10 libros mejor valorados de todos los tiempos
    top_books = (
        Book.objects.annotate(avg_score=Avg('reviews__score'))
        .order_by('-avg_score')[:10]
    )
    top_books = list(top_books)  # Convertir a lista para poder filtrar posteriormente

    # Obtener la reseña más popular y la peor reseña para cada uno de los 10 mejores libros
    top_books_with_reviews = []
    for book in top_books:
        highest_review = book.reviews.order_by('-score', '-number_of_upvotes').first()
        lowest_review = book.reviews.order_by('score', '-number_of_upvotes').first()
        top_books_with_reviews.append((book, highest_review, lowest_review))

    # Obtener los 50 libros más vendidos de todos los tiempos
    top_selling_books = (
        Book.objects.annotate(total_sales=Sum('sales__sale'))
        .order_by('-total_sales')[:50]
    )
    top_selling_books = list(top_selling_books)  # Convertir a lista para poder filtrar posteriormente

    # Obtener el total de ventas de cada autor y verificar si el libro estuvo en el top 5 el año de su publicación
    top_selling_books_with_authors = []
    for book in top_selling_books:
        author_sales = Sale.objects.filter(book__author=book.author).aggregate(total_sales=Sum('sale'))['total_sales']
        was_top_5 = book.sales.filter(year=book.date_of_publication.year).order_by('-sale')[:5]
        top_selling_books_with_authors.append((book, author_sales, was_top_5.exists()))

    return render(request, 'home.html', {
        'top_books_with_reviews': top_books_with_reviews,
        'top_selling_books_with_authors': top_selling_books_with_authors,
    })

    #return render(request, 'home.html')
