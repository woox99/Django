from django import forms
from app.models import *

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'publisher-name-input'}), # assign class name to form input
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'author-name-input'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'authors']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'book-title-input'}), 
            'publisher' : forms.Select(attrs={'class':'book-publisher-input'}), 
            'authors' : forms.SelectMultiple(attrs={'class':'book-authors-input'}), 
        }