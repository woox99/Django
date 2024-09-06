from django.db import models
from django.forms import ModelForm

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')

    def __str__(self):
        return self.title
    

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'authors']