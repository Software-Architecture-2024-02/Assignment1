import os
import django
from faker import Faker
import random

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from library.models import Author, Book, Review, Sale

# Crear una instancia de Faker
fake = Faker()

def clean_database():
    """Limpia las tablas antes de poblarlas."""
    Sale.objects.all().delete()
    Review.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()


def create_authors(n):
    authors = []
    for _ in range(n):
        author = Author.objects.create(
            name=fake.name(),
            date_of_birth=fake.date_of_birth(minimum_age=20, maximum_age=80),
            country_of_origin=fake.country(),
            short_description=fake.text(max_nb_chars=200)
        )
        authors.append(author)
    return authors

def create_books(authors, n):
    books = []
    for _ in range(n):
        author = random.choice(authors)
        book = Book.objects.create(
            name=fake.sentence(nb_words=4),
            summary=fake.text(max_nb_chars=500),
            date_of_publication=fake.date_between(start_date='-30y', end_date='today'),
            number_of_sales=random.randint(0, 10000),
            author=author
        )
        books.append(book)
    return books

def create_reviews(books):
    for book in books:
        num_reviews = random.randint(2, 10)
        for _ in range(num_reviews):
            Review.objects.create(
                book=book,
                review=fake.text(max_nb_chars=300),
                score=random.randint(1, 5),
                number_of_upvotes=random.randint(0, 1000)
            )

def create_sales(books):
    current_year = 2024
    for book in books:
        start_year = max(book.date_of_publication.year, current_year - 5)
        for year in range(start_year, current_year + 1):
            Sale.objects.create(
                book=book,
                year=year,
                sale=random.randint(0, 10000)
            )

if __name__ == '__main__':
    num_authors = 50
    num_books = 300

    # Limpiar la base de datos antes de poblarla
    clean_database()

    authors = create_authors(num_authors)
    books = create_books(authors, num_books)
    create_reviews(books)
    create_sales(books)
    
    print("Database populated successfully with fake data.")