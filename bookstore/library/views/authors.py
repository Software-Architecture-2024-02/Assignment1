from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Author
from ..forms import AuthorForm
from django.db.models import Avg, Count, Sum

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

class AuthorGrid(ListView):
    model = Author
    template_name = 'authors/author_grid.html'
    context_object_name = 'authors'

    def get_queryset(self):
        sort_by = self.request.GET.get('sort', 'name')
        sort_order = self.request.GET.get('order', 'asc')
        
        if sort_order == 'desc':
            sort_by = f'-{sort_by}'
        
        queryset = (
            Author.objects
            .annotate(
                num_books=Count('books'),
                avg_score=Avg('books__reviews__score'),
                total_sales=Sum('books__sales__sale')
            )
            .order_by(sort_by)
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort'] = self.request.GET.get('sort', 'name')
        context['order'] = self.request.GET.get('order', 'asc')
        return context
