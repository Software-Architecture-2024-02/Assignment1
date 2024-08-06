from django.urls import path
from ..views.search import SearchView

urlpatterns = [
    path('', SearchView.as_view(), name='search')
]
