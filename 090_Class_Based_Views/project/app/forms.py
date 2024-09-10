from django import forms
from app.models import *

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