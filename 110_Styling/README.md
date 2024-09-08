## Styling & DTL Reference

### Styling Forms
* <a href="https://docs.djangoproject.com/en/5.1/ref/forms/widgets/#module-django.forms.widgets" target="_blank">Widgets Documentation</a>
* <a href="https://docs.djangoproject.com/en/5.1/ref/forms/widgets/#built-in-widgets" target="_blank">Widgets List</a>
* <a href="https://docs.djangoproject.com/en/5.1/ref/forms/fields/#built-in-field-classes" target="_blank">Field Classes & Default Widgets List</a>
<!-- * <a href="" target="_blank">Template</a> -->

```py
# Assign class names to form inputs in forms.py

from django import forms
from app.models import *

# this is an example for a Model Form
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'publisher-name-input'}),
        }

# this is an example for a Class Form
class PublisherForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'name-input'}))
```

### Template Inheritance
* <a href="https://docs.djangoproject.com/en/5.1/ref/templates/language/#template-inheritance" target="_blank">Template Inheritance Documentation</a>

        <!-- Extends tag must be the first html in the document -->
        {% extends 'base_file_name.html' %}
