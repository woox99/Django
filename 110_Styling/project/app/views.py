from django.shortcuts import render, get_list_or_404
from django.urls import reverse_lazy
from app.forms import *

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from app.models import *

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'publishers'
    template_name = 'app/index.html'

class PublisherCreate(CreateView):
    model = Publisher
    form_class = PublisherForm
    # fields = ['name'] # not needed when using form_class
    template_name = 'app/publisher/publisher_create.html'

    def get_success_url(self):
        return reverse_lazy('app:publisher-detail', kwargs={'pk':self.object.pk})

class PublisherDetail(DetailView):
    model = Publisher
    template_name = 'app/publisher/publisher_detail.html'

class PublisherUpdate(UpdateView):
    model = Publisher
    form_class = PublisherForm
    # fields = ['name']
    template_name = 'app/publisher/publisher_update.html'

    def get_success_url(self):
        return reverse_lazy('app:publisher-detail', kwargs={'pk':self.object.pk})

class PublisherDelete(DeleteView):
    model = Publisher
    template_name = 'app/publisher/publisher_delete.html'
    success_url = reverse_lazy('app:publisher-list')


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    # fields = ['name']
    template_name = 'app/author/author_create.html'

    def get_success_url(self):
        return reverse_lazy('app:author-detail', kwargs={'pk':self.object.pk})
    
class AuthorDetail(DeleteView):
    model = Author
    template_name = 'app/author/author_detail.html'

class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    # fields = ['name']
    template_name = 'app/author/author_update.html'

    def get_success_url(self):
        return reverse_lazy('app:author-detail', kwargs={'pk':self.object.pk})
    
class AuthorDelete(DeleteView):
    model = Author
    template_name = 'app/author/author_delete.html'
    success_url = reverse_lazy('app:publisher-list')


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    # fields = ['title', 'publisher', 'authors']
    template_name = 'app/book/book_create.html'
    
    def get_success_url(self):
        return reverse_lazy('app:book-detail', kwargs={'pk':self.object.pk})

class BookDetail(DetailView):
    model = Book
    template_name = 'app/book/book_detail.html'

class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    # fields = ['title', 'publisher', 'authors']
    template_name = 'app/book/book_update.html'
    
    def get_success_url(self):
        return reverse_lazy('app:book-detail', kwargs={'pk':self.object.pk})

class BookDelete(DeleteView):
    model = Book
    template_name = 'app/book/book_delete.html'
    success_url = reverse_lazy('app:publisher-list')