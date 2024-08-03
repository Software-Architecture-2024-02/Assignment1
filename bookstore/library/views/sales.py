from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Sale
from ..forms import SaleForm

class SaleList(ListView):
    model = Sale
    template_name = 'sales/sale_list.html'

class SaleDetail(DetailView):
    model = Sale
    template_name = 'sales/sale_detail.html'

class SaleCreate(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sales/sale_form.html'

class SaleUpdate(UpdateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sales/sale_form.html'

class SaleDelete(DeleteView):
    model = Sale
    template_name = 'sales/sale_confirm_delete.html'
    success_url = '/sales/'
