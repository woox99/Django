from django.db import models
from django.urls import reverse

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('app:publisher-detail', kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('app:author-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('app:book-detail', kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title
    

