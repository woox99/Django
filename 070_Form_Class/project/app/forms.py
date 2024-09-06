from django import forms
from .models import *

class PublisherForm(forms.Form):
    name = forms.CharField(max_length=100)

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
