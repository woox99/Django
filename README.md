# Lesson Index
* Getting Started and Installation
    * <a href="https://docs.djangoproject.com/en/5.0/intro/install/" target="_blank">Quick Install Guide</a>
* Creating Django Project
* Basics 
    * URL Patterns
    * Views
    * Minimal Forms 
* Session Management
* URL Parameters
    * Query Parameters
* CRUD
    * Models
    * SQLite
    * Shell
* Related Objects ORM
    * OneToOne
    * OneToMany
    * ManyToMany
    * get_absolute_url 
* Form Class
* Model Forms
* Class Based Views
* Generic Views
* Styling
    * Load Static
    * Template Inheritance
* Admin
* Authentication
    * CBV
    * FBV
    * Multi App Project
* API
    * Django REST Framework


* Testing
    * Populating database with fake data (faker)
    * Coverage
* Slug
* Pagination
* File Upload
* Connecting MySQL
* Connect React
* AWS Deployment


# Common Commands

#### Virtual Envrionment

    py -m venv projectenv
    projectenv\scripts\activate

#### Django

    pip install django
    django-admin startproject 'projectname'
    py manage.py startapp 'app-name'
    py manage.py runserver

    py manage.py makemigrations
    py manage.py migrate

    py manage.py shell

#### Testing
    
    py manage.py test

    pip install Coverage
    coverage run --omit='*/venv/*' manage.py test
    coverage run manage.py test
    coverage html
    coverage report

#### Requirments

    pip install -r requirements.txt
    pip freeze > requirements.txt

#### MySQL

    mysql -u 'username' -p

    mysql> CREATE DATABASE 'db_name';
    mysql> EXIT;
