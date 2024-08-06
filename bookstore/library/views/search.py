# myapp/views/search.py
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from ..models import Book

class SearchView(View):
    template_name = 'search/search.html'

    def get(self, request):
        query = request.GET.get('q')
        if query:
            search_results = Book.objects.filter(summary__icontains=query)
        else:
            search_results = Book.objects.none()

        paginator = Paginator(search_results, 10)  # Show 10 books per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {'search_results': page_obj})
