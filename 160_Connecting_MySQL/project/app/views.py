from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Publisher, Author, Book

class IndexView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'app/index.html'


class PublisherCreate(CreateView):
    model = Publisher
    fields = ['name']
    template_name = 'app/publisher/create.html'
    success_url = reverse_lazy('app:index')


class AuthorCreate(CreateView):
    model = Author
    fields = ['name']
    template_name = 'app/author/create.html'
    success_url = reverse_lazy('app:index')


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'publisher', 'authors']
    template_name = 'app/book/create.html'
    success_url = reverse_lazy('app:index')
