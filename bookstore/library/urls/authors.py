from django.urls import path
from ..views.authors import AuthorList, AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete, AuthorGrid

urlpatterns = [
    path('', AuthorList.as_view(), name='author-list'),
    path('<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('add/', AuthorCreate.as_view(), name='author-create'),
    path('<int:pk>/edit/', AuthorUpdate.as_view(), name='author-update'),
    path('<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
    path('grid/', AuthorGrid.as_view(), name="author-grid")
]
