from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from app.models import *

class Index(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        return render(request, 'app/index.html', {'publishers':publishers})
    

class PublisherCreate(View):
    def get(self, request):
        form = PublisherForm
        return render(request, 'app/publisher_create.html', {'form':form})
    
    def post(self, request):
        publisher = PublisherForm(request.POST)
        if publisher.is_valid():
            publisher.save()
        return redirect('app:index')
    
class AuthorCreate(View):
    def get(self, request):
        form = AuthorForm
        return render(request, 'app/author_create.html', {'form':form})
    
    def post(self, request):
        author = AuthorForm(request.POST)
        if author.is_valid():
            author.save()
        return redirect('app:index')
    

class BookCreate(View):
    def get(self, request):
        form = BookForm
        return render(request, 'app/book_create.html', {'form':form})
    
    def post(self, request):
        book = BookForm(request.POST)
        if book.is_valid():
            book.save()
        return redirect('app:index')
    
