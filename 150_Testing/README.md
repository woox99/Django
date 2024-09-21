## Testing Reference

* <a href="https://docs.djangoproject.com/en/5.0/intro/tutorial05/" target="_blank">Testing Intro Documentation</a>
* <a href="https://docs.djangoproject.com/en/5.0/topics/testing/" target="_blank">Documentation</a>
* <a href="https://www.youtube.com/watch?v=swEjbCW9XDY&list=PLOLrQ9Pn6cay7t8VZ3wmn6QdAxzTx60F3&index=1" target="_blank">Video Tutorial 1</a>
* <a href="https://www.youtube.com/watch?v=GBgRMdjAx_c&list=PLOLrQ9Pn6cay7t8VZ3wmn6QdAxzTx60F3&index=2" target="_blank">Video Tutorial 2</a>
<!-- * <a href="" target="_blank">Template</a> -->

<br>

`NOTE:` If you want to make seperate test files: delete `test.py` -> create `tests` directory in `appname` -> create `__init__.py` file in newly created tests dir -> include your test files in newly created `__init__.py` file -> create your test files in `tests` dir (example: url.py for url tests)

```py
# __init__.py file
from .url import *
from .model import *
from .view import *
```


## Test Commands

Run all tests in all apps:

    py manage.py test

Isolate more specific tests to run:

* py manage.py test `appname`

* py manage.py test `appname`.tests.`filename`

* py manage.py test `appname`.tests.`filename`.`classname`

* py manage.py test `appname`.tests.`filename`.`classname`.`functionname`

## Coverage Commands

Omit venv from coverage report

    coverage run --omit='*/venv/*' manage.py test

Run test with coverage

    coverage run manage.py test
    
Update coverage html

    coverage html

Get coverage report in console

    coverage report

`NOTE:` to open coverage html in browser: run `coverage html` command -> find `htmlcov/index.html` -> right click `copy path` -> paste path in browser url


## Requirements

```
pip install coverage
```

