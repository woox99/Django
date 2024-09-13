from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app.models import Book
from .forms import BookForm

def index(request):
    return render(request, 'app/index.html')


def dashboard(request):
    books = Book.objects.all()
    return render(request, 'app/dashboard.html', {'books':books})


@login_required # displays 404 message if user is not logged in
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('app:dashboard')
    else:
        form = BookForm()
    return render(request, 'app/book/create.html', {'form':form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.owner != request.user:
        return redirect('app:dashboard')
    if request.method == 'POST':
            book.delete()
            return redirect('app:dashboard')
    return render(request, 'app/book/delete.html', {'book':book})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'app/book/detail.html', {'book':book})


def book_update(request, pk):
    book =get_object_or_404(Book, pk=pk)
    if book.owner != request.user:
        return redirect('app:dashboard')
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('app:book-detail', pk=pk)
        
    context = {
        'book' : book,
        'form' : BookForm(instance=book),
    }
    return render(request, 'app/book/update.html', context)