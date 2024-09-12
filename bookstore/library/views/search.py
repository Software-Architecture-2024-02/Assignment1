# myapp/views/search.py
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.conf import settings
from ..models import Book
from ..documents import BookDocument

class SearchView(View):
    template_name = 'search/search.html'

    def get(self, request):
        query = request.GET.get('q')
        if query:
            if settings.SEARCH_ENGINE == 'opensearch':
                try:
                    # Search in OpenSearch
                    search_results = BookDocument.search().query('match', summary=query)
                    search_results = search_results.execute()
                    # Manually create a list of books with URLs
                    books_with_urls = []
                    for hit in search_results:
                        book_id = hit.meta.id  # Access ID from meta
                        book = Book.objects.get(pk=book_id)  # Get the book instance by ID
                        books_with_urls.append({
                            'name': book.name,
                            'summary': book.summary,
                            'get_absolute_url': book.get_absolute_url()
                        })
                    print("SEARCHED WITH OPENSEARCH")
                except:
                    # Search in PostgreSQL
                    search_results = Book.objects.filter(summary__icontains=query)
                    books_with_urls = [{
                        'name': book.name,
                        'summary': book.summary,
                        'get_absolute_url': book.get_absolute_url()
                    } for book in search_results]

            else:
                # Search in PostgreSQL
                search_results = Book.objects.filter(summary__icontains=query)
                books_with_urls = [{
                    'name': book.name,
                    'summary': book.summary,
                    'get_absolute_url': book.get_absolute_url()
                } for book in search_results]
        else:
            books_with_urls = []

        paginator = Paginator(books_with_urls, 10)  # Show 10 books per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {'search_results': page_obj})