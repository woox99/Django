from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('add-publisher/', PublisherCreate.as_view(), name='publisher-create'),
    path('publisher/<int:pk>', PublisherDetail.as_view(), name='publisher-detail'),
    path('delete-publisher/<int:pk>', PublisherDelete.as_view(), name='publisher-delete'),
    path('update-publisher/<int:pk>', PublisherUpdate.as_view(), name='publisher-update'),
    path('add-author/', AuthorCreate.as_view(), name='author-create'),
    path('add-book/', BookCreate.as_view(), name='book-create'),
]