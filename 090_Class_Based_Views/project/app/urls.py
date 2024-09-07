from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('add-publisher/', PublisherCreate.as_view(), name='publisher-create'),
    path('add-author/', AuthorCreate.as_view(), name='author-create'),
    path('add-book/', BookCreate.as_view(), name='book-create'),
]