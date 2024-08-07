from django.urls import path
from ..views.books import BookList, BookDetail, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('add/', BookCreate.as_view(), name='book-create'),
    path('<int:pk>/edit/', BookUpdate.as_view(), name='book-update'),
    path('<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
]
