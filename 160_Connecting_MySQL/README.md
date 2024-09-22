## Connect MySQL Reference

* <a href="https://docs.djangoproject.com/en/5.0/ref/databases/#connecting-to-the-database" target="_blank">Documentation</a>
* <a href="https://www.geeksforgeeks.org/how-to-integrate-mysql-database-with-django/" target="_blank">Article - How to integrate Mysql database with Django</a>
<!-- * <a href="" target="_blank">Template</a> -->

## Steps
1. Install ``mysqlclient``
    ```
    pip install mysqlclient
    ```

2. Install ``python-dotenv``
    ```
    pip install python-dotenv
    ```

5. Create ``.env`` file
    ```env
    DB_NAME='db_name'
    DB_USER='username'
    DB_PASSWORD='password'
    DB_HOST=localhost
    DB_PORT=3306
    ```

4. Configure ``settings.py``
    ```python
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    #... 

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
    }
    ```


6. Create MySQL database with the same name. Replace ``username`` & ``db_name``

    ```
    mysql -u 'username' -p

    mysql> CREATE DATABASE 'db_name';
    mysql> EXIT;
    ```

7. Migrate database
    ```
    py manage.py makemigrations
    py manage.py migrate
    ```

## Requirements

```
pip install -r requirements.txt
```
```
pip install mysqlclient
```
```
pip install python-dotenv
```
## MySQL command-line client
Replace ``username`` & ``db_name``
```
mysql -u 'username' -p

mysql> CREATE DATABASE 'db_name';
mysql> EXIT;
```
<!-- * <a href="" target="_blank">Template</a> -->