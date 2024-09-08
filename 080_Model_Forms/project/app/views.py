from django.shortcuts import render, redirect
from app.models import *
from app.forms import *

def index(request):
    publishers = Publisher.objects.all()
    return render(request, 'app/index.html', {'publishers':publishers})

def publisher_create(request):
    form = PublisherForm()
    if request.method == 'POST':
        publisher = PublisherForm(request.POST)
        if publisher.is_valid():
            publisher.save()
        return redirect('app:index')
    return render(request, 'app/publisher_create.html', {'form':form})

def author_create(request):
    form = AuthorForm()
    if request.method == 'POST':
        author = AuthorForm(request.POST)
        if author.is_valid():
            author.save()
            return redirect('app:index')
    return render(request, 'app/author_create.html', {'form':form})

def book_create(request):
    form = BookForm
    if request.method == 'POST':
        book = BookForm(request.POST)
        if book.is_valid():
            book.save()
        return redirect('app:index')
    return render(request, 'app/book_create.html', {'form':form})