from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Book
from ..forms import BookForm

class BookList(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'

class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'

class BookDelete(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = '/books/'
