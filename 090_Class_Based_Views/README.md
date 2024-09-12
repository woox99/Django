# Class Based Views References

* <a href="https://docs.djangoproject.com/en/5.1/topics/class-based-views/" target="_blank">Topic Guide Documentation</a>
* <a href="https://docs.djangoproject.com/en/5.1/ref/class-based-views/" target="_blank">Views Reference</a>
* <a href="https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#form-handling-with-class-based-views" target="_blank">Handling Forms CBV</a>
<!-- * <a href="" target="_blank">Template</a> -->

`NOTE:` Import `ModelForm` in `models.py` file, and create Model Form inside `models.py`

```py
from django.db import models
from django.forms import ModelForm


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']
```

### `Backlog:`

* Make view, delete, and update views



