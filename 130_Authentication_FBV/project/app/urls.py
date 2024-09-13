from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-book/', views.book_create, name='book-create'),
    path('delete-book/<int:pk>/', views.book_delete, name='book-delete'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('edit-book/<int:pk>/', views.book_update, name='book-update'),
]