from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('book/<int:pk>/', views.book_view, name='book-view'),
    path('add-book/', views.book_create, name='add-book'),
    path('delete-book/<int:pk>/', views.book_delete, name='delete-book'),
    path('edit-book/<int:pk>/', views.book_update, name='edit-book'),
]