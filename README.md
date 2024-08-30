# Index
* Getting Started and Installation
    * Overview
    * Prerequisites
    * Installation
* Creating Django Project
    * App Configuration
    * Starting Development Server
* Basics
    * Templates & DTL
    * Views
    * URL Patterns
* Request Handling
    * URL Parameters (Path Variables)
    * Query Parameters
* Session Management and Caching
* Styling
    * Load Static
* Forms
    * csrf tokens
* CRUD
    * Models
    * SQLite
    * DB Browser
    * Shell
* Authetication
    * Validation
* Testing
    * Populating database with fake data (faker)
    * Coverage
* Related Objects ORM
    * OneToOne
    * OneToMany
    * ManyToMany
    * get_absolute_url
* Multi App Project
* Built-in Users
* Built-in Admin and Authorization
* Built-in Forms
* ModelForms
* Class Based Views (CBV)
    * Generic Views
* Template Inheritance
    * Django Template Language (revisit)
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

    py manage.py test

    py manage.py shell

#### Requirments

    pip install -r requirements.txt
    pip freeze > requirements.txt

#### MySQL

    mysql -u 'username' -p

    mysql> CREATE DATABASE 'db_name';
    mysql> EXIT;
