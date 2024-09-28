from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Book

class IndexView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'app/index.html'


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'publisher']
    template_name = 'app/book/create.html'
    success_url = reverse_lazy('app:index')


class BookDetail(DetailView):
    model = Book
    template_name = 'app/book/detail.html'
