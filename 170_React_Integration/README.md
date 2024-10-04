# React Integration Reference

* <a href="https://www.youtube.com/watch?v=F9o4GSkSo40" target="_blank">Tutorial Video</a>
* <a href="https://dev.to/nagatodev/how-to-connect-django-to-reactjs-1a71" target="_blank">Tutorial Article</a>

# Steps

* Create Django project

        django-admin startproject projectname

* Cd into project directory

        cd projectname

* Create React app

        npx create-react-app reactappname

* Cd into react directory

        cd reactappname

* Run build

        npm run build

* Open `project/settings.py` and add the following:

    ```py
    import os # add this line

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'reactappname', 'build')], # change reactappname to name of react app
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'reactappname', 'build', 'static')] # add this line, change reactappname
    ```

* Create api app in `project/` directory

        py manage.py startapp api

* Create `urls.py` file in `project/api` dir

    ```py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index')
    ]
    ```

* In `project/api/views.py` create view that renders `index.html` from react app

    ```py
    from django.shortcuts import render

    def index(request):
        return render(request, 'index.html')
    ```

* Include app in `project/settings.py`

    ```py
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        'api', # add this
    ]
    ```

* Include `api/urls.py` in `project/urls.py` file:

    ```py
    from django.contrib import admin
    from django.urls import path, include # import include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path('', include('api.urls')) # include this
    ]
    ```

* Runserver and navigate to `http://localhost:8000/` to make sure django is serving the django app

        py manage.py runserver

* During react development, use the react dev server and navigate to `http://localhost:3000/`

        npm start


# Common Commands

        npx create-react-app reactappname
        npm run build
        npm start

`NOTE:` Make sure to exclude `/build` from .gitignore file



