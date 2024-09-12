import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

# Import models and OpenSearch document
from library.models import Book
from library.documents import BookDocument

def populate_opensearch():
    # Get all books from the PostgreSQL database
    books = Book.objects.all()

    # Loop through the books and save them to OpenSearch
    for book in books:
        # Prepare the document for indexing in OpenSearch
        book_document = BookDocument(
            meta={'id': book.id},  # Set the document ID to match the book's ID
            name=book.name,
            summary=book.summary,
            date_of_publication=book.date_of_publication,
            number_of_sales=book.number_of_sales,
            author={
                'id': book.author.id,
                'name': book.author.name,
            }
        )
        
        # Save (index) the document in OpenSearch
        book_document.save()

    print('Successfully populated OpenSearch index with books.')

# Run the function to populate OpenSearch
if __name__ == "__main__":
    populate_opensearch()