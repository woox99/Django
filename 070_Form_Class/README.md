# Form Class References

* <a href="https://docs.djangoproject.com/en/5.1/topics/forms/#the-django-form-class" target="_blank">Form Class Documentation</a>
* <a href="https://docs.djangoproject.com/en/5.1/ref/forms/fields/#module-django.forms.fields" target="_blank">Form Fields</a>
<!-- * <a href="" target="_blank">Template</a> -->

`NOTE:` Create `forms.py` file in `project/app` directory

```py
from django import forms
from .models import *

class PublisherForm(forms.Form):
    name = forms.CharField(max_length=100)  # These are form fields

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all()) # One to one relationship
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all()) # One to many relationship
```

