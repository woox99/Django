from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Book
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(TemplateView):
    template_name = 'app/index.html'


class DashboardView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'app/dashboard.html'


@method_decorator(login_required, name='dispatch')
class BookCreate(CreateView):
    model = Book
    fields = ['title']
    template_name = 'app/book/create.html'
    success_url = reverse_lazy('app:dashboard')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.owner = self.request.user
        book.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class BookDetail(DetailView):
    model = Book
    template_name = 'app/book/detail.html'


class BookDelete(DeleteView):
    model = Book
    template_name = 'app/book/delete.html'
    success_url = reverse_lazy('app:dashboard')

    def dispatch(self, request, *args, **kwargs):
        book = self.get_object()
        if book.owner != request.user:
            return redirect('app:dashboard')
        return super().dispatch(request, *args, **kwargs)
    

class BookUpdate(UpdateView):
    model = Book
    fields = ['title']
    template_name = 'app/book/update.html'
    
    def dispatch(self, request, *args, **kwargs):
        book = self.get_object()
        if book.owner != request.user:
            return redirect('app:dashboard')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('app:book-detail', kwargs={'pk':self.object.pk})
