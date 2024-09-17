from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-book', BookCreate.as_view(), name='book-create'),
]