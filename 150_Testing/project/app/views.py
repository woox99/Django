from django.shortcuts import render, redirect, get_object_or_404
from .models import Publisher, Author, Book
from .forms import BookForm

def index_view(request):
    books = Book.objects.all()
    return render(request, 'app/index.html', {'books':books})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    form = BookForm()
    return render(request, 'app/book/create.html', {'form':form})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'app/book/detail.html', {'book':book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('app:index')
    return render(request, 'app/book/delete.html', {'book':book})
