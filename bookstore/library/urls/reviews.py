from django.urls import path
from ..views.reviews import ReviewList, ReviewDetail, ReviewCreate, ReviewUpdate, ReviewDelete

urlpatterns = [
    path('', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('add/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/edit/', ReviewUpdate.as_view(), name='review-update'),
    path('<int:pk>/delete/', ReviewDelete.as_view(), name='review-delete'),
]
