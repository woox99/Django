from django.contrib import admin
from app.models import *

class BookAdmin(admin.ModelAdmin):
    # adds field column on model list page
    list_display = ["title", "publisher", 'published_date', 'pages']

    # adds filter box on model list page
    list_filter = ['publisher', 'published_date']

    # groups fields together with different fieldsets
    fieldsets = [
        ('Book Details', {"fields": ["title", 'publisher', 'authors', 'pages']}),
        ("Date information", {"fields": ["published_date"]}),
    ]

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book, BookAdmin) # include the BookAdmin alterations class