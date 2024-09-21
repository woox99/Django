from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('add-book/', views.book_create, name='book-create'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('delete-book/<int:pk>/', views.book_delete, name='book-delete'),
]