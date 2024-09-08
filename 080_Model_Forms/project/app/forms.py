from django import forms
from app.models import *

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

    widgets = {
        'name' : forms.TextInput(attrs={'class':'name-input'}) # assigns class name to form input
    }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'authors']