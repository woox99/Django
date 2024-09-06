from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    publishers = Publisher.objects.all()
    return render(request, 'app/index.html', {'publishers':publishers})

def publisher_create(request):
    form = PublisherForm
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        # print(form) # prints the form html element
        if form.is_valid():
            name = form.cleaned_data['name']
            Publisher.objects.create(name=name)
        return redirect('app:index')
    return render(request, 'app/publisher_create.html', {'form':form})

def author_create(request):
    form = AuthorForm
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Author.objects.create(name=name)
            return redirect('app:index')
    return render(request, 'app/author_create.html', {'form':form})

def book_create(request):
    form = BookForm
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            publisher = form.cleaned_data['publisher']
            authors = form.cleaned_data['authors']

            book = Book.objects.create(title=title, publisher=publisher)
            book.authors.set(authors)
        return redirect('app:index')
    return render(request, 'app/book_create.html', {'form':form})