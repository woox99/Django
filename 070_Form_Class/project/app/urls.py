from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-publisher', views.publisher_create, name='publisher-create'),
    path('add-author', views.author_create, name='author-create'),
    path('add-book', views.book_create, name='book-create'),
]