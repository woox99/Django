from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Book
from django.core.paginator import Paginator

class IndexView(ListView):
    model = Book
    template_name = 'app/index.html'

    def get_context_data(self):
        books = Book.objects.all()
        paginator = Paginator(books, 2)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj':page_obj}
        return context

class BookCreate(CreateView):
    model = Book
    fields = ['title']
    template_name = 'app/book_create.html'
    success_url = reverse_lazy('index')
