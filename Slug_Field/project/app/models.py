from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('app:book-detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title


@receiver(pre_save)
def generate_slug(sender, instance, **kwargs):
    if hasattr(instance, 'slug') and hasattr(instance, '__str__'):
        if not instance.pk: # Only generate slug for new objects
            slug = slugify(instance.__str__())
            base_slug = slug
            counter = 2
            while sender.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            instance.slug = slug 