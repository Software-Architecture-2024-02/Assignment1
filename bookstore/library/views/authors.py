from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Author
from ..forms import AuthorForm

class AuthorList(ListView):
    model = Author
    template_name = 'authors/author_list.html'

class AuthorDetail(DetailView):
    model = Author
    template_name = 'authors/author_detail.html'

class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/author_form.html'

class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/author_form.html'

class AuthorDelete(DeleteView):
    model = Author
    template_name = 'authors/author_confirm_delete.html'
    success_url = '/authors/'
