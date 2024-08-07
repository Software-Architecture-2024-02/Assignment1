from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Review
from ..forms import ReviewForm

class ReviewList(ListView):
    model = Review
    template_name = 'reviews/review_list.html'

class ReviewDetail(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'

class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

class ReviewUpdate(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

class ReviewDelete(DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    success_url = '/reviews/'
