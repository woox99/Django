from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('add-book/', BookCreate.as_view(), name='book-create'),
    path('delete-book/<int:pk>/', BookDelete.as_view(), name='book-delete'),
    path('edit-book/<int:pk>/', BookUpdate.as_view(), name='book-update'),
]