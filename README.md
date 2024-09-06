# Lesson Index
* Getting Started and Installation
    * Overview
    * Prerequisites
    * Installation
* Creating Django Project
    * App Configuration
    * Starting Development Server
* Forms
    * Views
    * URL Patterns
    * Templates
    * DTL Variables
* Session Management
* Request Handling
    * URL Parameters (Path Variables)
    * Query Parameters
* CRUD
    * Models
    * SQLite
    * DB Browser
    * Shell
* Related Objects ORM
    * OneToOne
    * OneToMany
    * ManyToMany
    * get_absolute_url 

* Styling
    * Load Static
* Authetication
    * Validation
* Multi App Project
* Built-in Users
* Built-in Admin and Authorization
* Built-in Forms
* ModelForms
* Class Based Views (CBV)
    * Generic Views
* Template Inheritance
    * Django Template Language (revisit)
* Testing
    * Populating database with fake data (faker)
    * Coverage
* API
    * Django REST Framework
    * Connecting React
* Connecting MySQL
* AWS Deployment

#### Extras
* Slug
* Pagination

<br>

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
