from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.publisher_list, name='publisher-list'),
    path('add-publisher', views.publisher_create, name='publisher-create'), 
    path('publisher/<int:pk>/', views.publisher_detail, name='publisher-detail'), 
    path('edit-publisher/<int:pk>/', views.publisher_update, name='publisher-update'), 
    path('delete-publisher/<int:pk>/', views.publisher_delete, name='publisher-delete'),
    path('add-book/', views.book_create, name='book-create'), 
    path('book/<int:pk>/', views.book_detail, name='book-detail'), 
    path('edit-book/<int:pk>/', views.book_update, name='book-update'), 
    path('delete-book/<int:pk>/', views.book_delete, name='book-delete'), 
    path('add-author/', views.author_create, name='author-create'), 
    path('author/<int:pk>/', views.author_detail, name='author-detail'),
    path('edit-author/<int:pk>/', views.author_update, name='author-update'),
    path('delete-author/<int:pk>/', views.author_delete, name='author-delete'),
]