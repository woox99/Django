from django.db import models

from django.db import models
from django.forms import ModelForm


GENDER_CHOICES = {
    'MALE' : 'Male',
    'FEMALE' : 'Female',
}

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='male')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')
    pages = models.IntegerField(default=100)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    


