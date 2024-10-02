from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from app.models import *
from app.forms import *

class Index(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        return render(request, 'app/index.html', {'publishers':publishers})
    

class PublisherCreate(View):
    def get(self, request):
        form = PublisherForm()
        return render(request, 'app/publisher/publisher_create.html', {'form':form})
    
    def post(self, request):
        form = PublisherForm(request.POST)
        if form.is_valid():
            publisher = form.save()
            return redirect('app:index')
        return render(request, 'app/publisher/publisher_create.html', {'form':form})
    

class PublisherDetail(View):
    def get(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        return render(request, 'app/publisher/publisher_detail.html', {'publisher':publisher})


class PublisherDelete(View):
    def get(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        return render(request, 'app/publisher/publisher_delete.html', {'publisher':publisher})
    
    def post(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        publisher.delete()
        return redirect('app:index')


class PublisherUpdate(View):
    def get(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        form = PublisherForm(instance=publisher)
        context = {
            'form' : form,
            'publisher' : publisher,
        }
        return render(request, 'app/publisher/publisher_update.html', context)

    def post(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('app:publisher-detail', pk=pk)
        context = {
            'form' : form,
            'publisher' : publisher,
        }
        return render(request, 'app/publisher/publisher_update.html', context)


class AuthorCreate(View):
    def get(self, request):
        form = AuthorForm()
        return render(request, 'app/author_create.html', {'form':form})
    
    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('app:index')
        return render(request, 'app/author_create.html', {'form':form})
    

class BookCreate(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'app/book_create.html', {'form':form})
    
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('app:index')
        return render(request, 'app/book_create.html', {'form':form})

