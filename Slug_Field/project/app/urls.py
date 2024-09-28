from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-book', BookCreate.as_view(), name='book-create'),
    path('book/<slug:slug>/', BookDetail.as_view(), name='book-detail'),
]