# CRUD References

* <a href="https://docs.djangoproject.com/en/5.0/intro/tutorial02/" target="_blank">Documentation</a>
<!-- * <a href="" target="_blank">Template</a> -->

Migrate database after setting up models to begin working with models

    py manage.py makemigrations
    py manage.py migrate

Access the database API from the terminal

    py manage.py shell

```py
>>> from app.models import Book
>>> b = Book.objects.create(title='Test Book',publisher='Test Publisher',author='Test Author')
>>> b
<Book: Test Book>
>>> b.title
'Test Book'
>>> b.title = 'Test Title'
>>> b.save()
>>> b.title
'Test Title'
>>> exit()
```