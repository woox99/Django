from django.shortcuts import render, redirect, get_object_or_404

from .models import Publisher, Author, Book

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'app/index.html', {'publishers':publishers})


def publisher_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        publisher = Publisher.objects.create(name=name)
        return redirect(publisher.get_absolute_url())
    return render(request, 'app/publisher/publisher_create.html')


def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, 'app/publisher/publisher_detail.html', {'publisher':publisher})


def publisher_update(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.name = request.POST['name']
        publisher.save()
        return redirect(publisher.get_absolute_url())
    return render(request, 'app/publisher/publisher_update.html', {'publisher':publisher})


def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('app:publisher-list')
    return render(request, 'app/publisher/publisher_delete.html', {'publisher':publisher})


def book_create(request):
    context = {
        'publishers' : Publisher.objects.all(),
        'authors' : Author.objects.all()
    }
    if request.method == 'POST':
        title = request.POST['title']
        publisher = Publisher.objects.get(pk=request.POST['publisher_id'])
        book = Book.objects.create(title=title, publisher=publisher)
        
        author_ids = request.POST.getlist('author_ids')
        if author_ids:
            authors = Author.objects.filter(pk__in=author_ids)
            book.authors.set(authors)
        return redirect(book.get_absolute_url())
    return render(request, 'app/book/book_create.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'app/book/book_detail.html', {'book':book})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book' : book,
        'book_authors_ids_list' : list(book.authors.values_list('id', flat=True)),
        'publishers' : Publisher.objects.all(),
        'authors' : Author.objects.all()
    }
    if request.method == 'POST':
        title = request.POST['title']
        publisher = Publisher.objects.get(pk=request.POST['publisher_id'])
        book.title = title
        book.publisher = publisher
        
        author_ids = request.POST.getlist('author_ids')
        if author_ids:
            authors = Author.objects.filter(pk__in=author_ids)
            book.authors.set(authors)
            book.save()
        return redirect(book.get_absolute_url())
    return render(request, 'app/book/book_update.html', context)


def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
        return redirect('app:publisher-list')
    return render(request, 'app/book/book_delete.html', {'book':book})


def author_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        author = Author.objects.create(name=name)
        return redirect(author.get_absolute_url())
    return render(request, 'app/author/author_create.html')
    

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'app/author/author_detail.html', {'author':author})


def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.name = request.POST['name']
        author.save()
        return redirect(author.get_absolute_url())
    return render(request, 'app/author/author_update.html', {'author':author})


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('app:publisher-list')
    return render(request, 'app/author/author_delete.html', {'author':author})
