# Model Forms References

* <a href="https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/" target="_blank">ModelForm Documentation</a>
<!-- * <a href="" target="_blank">Template</a> -->

#### Import `ModelForm` in `models.py` file, and create Model Form inside `models.py`

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

