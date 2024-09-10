# Admin GUI Reference
### Links

* <a href="https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#module-django.contrib.admin" target="_blank">Admin Site | Documentation</a>
* <a href="https://docs.djangoproject.com/en/5.0/intro/tutorial07/#customize-the-admin-form" target="_blank">Customizing Admin Forms | Documentation</a>
<!-- * <a href="" target="_blank">Template</a> -->

<hr>

### Steps:

Create models, and migrate database:

    py manage.py makemigrations
    py manage.py migrate

Import and register models in `projectname/appname/admin.py` :

```py
from django.contrib import admin
from app.models import *

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
```

Create superuser:

    py manage.py createsuperuser

Navigate to admin URL:

`http://localhost:8000/admin` 

<hr>

### Backlog:

* Install admin graphing package
    * Track site views
    * Track site visits
