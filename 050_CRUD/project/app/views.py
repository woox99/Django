from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Book

def book_list(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request, 'app/index.html', context)

def book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'app/book_view.html', {'book':book})

def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        publisher = request.POST['publisher']
        author = request.POST['author']
        book = Book.objects.create(title=title, publisher=publisher, author=author)
        return redirect(reverse('app:book-view', args=[book.pk]))
    return render(request, 'app/book_create.html') # if method == GET

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(reverse('app:book-list'))
    return render(request, 'app/book_delete.html', {'book':book})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.publisher = request.POST['publisher']
        book.author = request.POST['author']
        book.save()
        return redirect(reverse('app:book-view', args=[book.pk]))
    return render(request, 'app/book_update.html', {'book':book})