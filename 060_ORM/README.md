# ORM References

* <a href="https://docs.djangoproject.com/en/5.0/topics/db/models/#relationships" target="_blank">Model Relationships Documentation</a>
* <a href="https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types" target="_blank">Fields Types Reference</a>
* <a href="https://docs.djangoproject.com/en/5.0/topics/db/queries/" target="_blank">Making Queries Documentation</a>
* <a href="https://github.com/chrisdl/Django-QuerySet-Cheatsheet?tab=readme-ov-file" target="_blank">Cheatsheet for Django QuerySets</a>
* <a href="https://docs.djangoproject.com/en/5.1/ref/models/instances/#get-absolute-url" target="_blank">get_absolute_url()</a>
<!-- * <a href="" target="_blank">Template</a> -->

`NOTE:` Migrate database after setting up models to begin working with models

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