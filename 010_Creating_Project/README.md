# Creating Project Reference
<!-- * <a href="" target="_blank">Template</a> -->

## Steps

1. Create a new directoy with project name

2. cd into `projectname\` directory

3. Create & activate virtual environment

        py -m venv projectenv
        projectenv\scripts\activate

4. Install django

        pip install django

5. Create project 

        django-admin startproject 'projectname'

6. cd in `projectname\` directory, and create a new app

        py manage.py startapp 'app-name'

7. Open `projectname\settings.py` and add app configuration to INSTALLED_APPS

    ```python
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        'app', # add app config here
    ]
    ```

8. Open `projectname\projectname\urls.py` and include URL pattern for the new app

    ```python
    from django.contrib import admin
    from django.urls import path, include # import include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path('app/', include('app.urls')), # add pattern here
    ]
    ```

9. Create new `urls.py` file in the `projectname\appname\` directory:

    ```py
    from django.urls import path
    from . import views

    app_name = 'app'

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```

10. Open `projectname\appname\views.py` and create your views:

    ```py
    from django.shortcuts import render

    def index(request):
        return render(request, 'app/index.html')
    ```

11. Create a templates directory with the structure `templates\appname\`

12. Create `templates\appname\index.html` file

12. Run server

        py manage.py runserver

13. Open web browser and navigate to `http://localhost:8000/app/`