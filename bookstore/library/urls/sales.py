from django.urls import path
from ..views.sales import SaleList, SaleDetail, SaleCreate, SaleUpdate, SaleDelete

urlpatterns = [
    path('', SaleList.as_view(), name='sale-list'),
    path('<int:pk>/', SaleDetail.as_view(), name='sale-detail'),
    path('add/', SaleCreate.as_view(), name='sale-create'),
    path('<int:pk>/edit/', SaleUpdate.as_view(), name='sale-update'),
    path('<int:pk>/delete/', SaleDelete.as_view(), name='sale-delete'),
]
