from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('', PublisherList.as_view(), name='publisher-list'),
    path('add-publisher/', PublisherCreate.as_view(), name='publisher-create'),
    path('publisher/<int:pk>/', PublisherDetail.as_view(), name='publisher-detail'),
    path('edit-publisher/<int:pk>/', PublisherUpdate.as_view(), name='publisher-update'),
    path('delete-publisher/<int:pk>/', PublisherDelete.as_view(), name='publisher-delete'),
    path('add-author/', AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('edit-author/<int:pk>/', AuthorUpdate.as_view(), name='author-update'),
    path('delete-author/<int:pk>/', AuthorDelete.as_view(), name='author-delete'),
    path('add-book/', BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('update-book/<int:pk>/', BookUpdate.as_view(), name='book-update'),
    path('delete-book/<int:pk>/', BookDelete.as_view(), name='book-delete'),
]