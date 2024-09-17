from django.urls import path
from .views import *

urlpatterns = [
    path('publishers', PublisherList.as_view(), name='publisher-list'),
    path('publisher/<int:pk>/', PublisherDetail.as_view(), name='publisher-detail'),
    path('authors', AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('books', BookList.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]